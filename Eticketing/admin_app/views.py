from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseForbidden
from django.contrib.auth.decorators import login_required
from ticket_app.forms import *
from .forms import UserUpdateForm, UserForm
from ticket_app.models import Event, Ticket
from django.contrib.auth.hashers import make_password
from ticket_app.views import *
from django.db.models import Sum, Count


def admin_home(request):
    if request.user.is_authenticated and request.user.is_superuser:
       
        return render(request, 'admin_home.html')
    
    elif request.method == "POST":
        # Handle sign-in form submission
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            if user.is_superuser:  # Only allow superusers to log in
                login(request, user)
                return redirect('admin_app:admin_home')
            else:
                form.add_error(None, "You don't have permission to access the admin area.")
    else:
        # Display sign-in form
        form = AuthenticationForm()
    
    return render(request, 'sign_in.html', {'form': form})
    

@login_required(login_url= "/sign_in")
def user_list(request):
    user_groups = list(Group.objects.filter(user=request.user).values_list('name', flat=True))
    if not request.user.is_superuser:
        return HttpResponseForbidden("You are not authorized to access this page.")
    users = User.objects.filter(is_superuser=False)
    print(users)
    return render(request, 'user_list.html', {'users': users, 'user_groups': user_groups})

#but the issue is that you are hashing the password (make_password) but not actually applying it to the saved user.
#  The form.save() call directly saves the user with the unprocessed password field from the form.
def add_user(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False) # Create the user object but don't save yet
            user.password = make_password(form.cleaned_data['password'])
            user.save()
            return redirect('admin_app:user_list')
    else:
        form = UserForm()
    return render(request, 'add_user.html', {'form': form})

def detail_view(request, id):
    user = get_object_or_404(User, id=id)
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('admin_app:user_detail', id=user.id) 
    else:
        form = UserUpdateForm(instance=user)
    return render(request, 'detail_view.html', {'form': form, 'user': user})

def delete_user(request, id):
    user = get_object_or_404(User, id=id)
    if request.method == "POST":
        user.delete()
        return redirect('admin_app:user_list')

def admin_login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            if user.is_staff:  # Ensure only admin users can log in
                login(request, user)
                return redirect('user_list')  # Redirect to the dashboard
            else:
                form.add_error(None, "You do not have admin privileges.")
    else:
        form = AuthenticationForm()
    return render(request, 'admin_login.html', {'form': form})

from django.shortcuts import render

def admin_dashboard(request):
    return render(request, 'dashboard.html')


def event_list(request):
    
    events = Event.objects.filter()
    return render(request, 'event_list.html', {'events': events})


def ticket_sales(request, id):
    event = get_object_or_404(Event, id=id)
    result = Ticket.objects.filter(event_details__event_title="e4").aggregate(total_ticket_quantity=Sum('ticket_quantity', default = 0))
    ticket_sales = result['total_ticket_quantity']
    remaining_seats = event.event_capacity - ticket_sales
    revenue_generated = ticket_sales * event.event_price

    return render (request, 'ticket_sales.html', {'event': event,'ticket_sales': ticket_sales, 'remaining_seats': remaining_seats,'revenue_generated': revenue_generated})

def event_list_ticket(request):
    events = Event.objects.all()
    return render(request, 'event_list_ticket.html', {'events': events})

