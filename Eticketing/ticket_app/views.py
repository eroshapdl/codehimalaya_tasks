from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from ticket_app.models import Event, Ticket
from ticket_app.forms import *
from django.contrib.auth.decorators import login_required, user_passes_test
from ticket_app.decorators import authenticated_user, group_required
from django.contrib import messages
from django.contrib.auth.models import Group
from django.contrib.auth.models import User
from django.contrib.sessions.models import Session

def homepage(request):
    return HttpResponse ('this is homepage')






def logout_view(request):
    logout(request)
   
    # clear the user's session data
    Session.objects.filter(session_key=request.session.session_key).delete()
    print("Session ID after logout:", request.session.session_key)
    if not request.user.is_authenticated:
        print("User is logged out successfully!")
    return redirect('ticket_app:sign_in')


@login_required(login_url="/sign_in")
def event_view (request, id):
    event = get_object_or_404(Event, id=id)
   
    if request.method == 'POST':
        form = EventCreateForm(request.POST, instance=event)
        if form.is_valid():
            if Event.objects.exclude(id=event.id).filter(event_title=form.cleaned_data['event_title']).exists():
                form.add_error('event_title', 'An event with this title already exists.')
            else:
                form.save()
                return redirect('ticket_app:event_view', id=id)
            
            
        
    else:
        form = EventCreateForm(instance=event)
    return render (request, 'event_view.html', {'form': form, 'event':event})

@login_required(login_url= "/sign_in")
def event_list(request):
    events = Event.objects.all()
    user_groups = list(Group.objects.filter(user=request.user).values_list('name', flat=True))
    print(user_groups)
    return render(request, 'event_list.html', {'events': events,'user_groups': user_groups})

def admin_check(user):
    return user.is_superuser

@group_required('Admin')
@user_passes_test(admin_check, login_url= "/sign_in")
def admin_dashboard(request):
    
    return render (request, 'admin_app:admin_home')

@group_required('Admin')
@login_required(login_url="/sign_in")
#@user_passes_test(admin_check, login_url= "/login")
def event_create_form (request):
    print(f"FUnc User: {request.user}, Groups: {request.user.groups.values_list('name', flat=True)}")
    form = EventCreateForm()
    if request.method == 'POST':
        form = EventCreateForm (request.POST)
        if form.is_valid():
           # print (form.cleaned_data)
            event_title = form.cleaned_data ["event_title"]
            event_description = form.cleaned_data ["event_description"]

            event_date = form.cleaned_data ["event_date"]
            event_time = form.cleaned_data ["event_time"]
            event_address = form.cleaned_data ["event_address"]
            event_capacity = form.cleaned_data ["event_capacity"]
            event_price = form.cleaned_data ["event_price"]
            new_event = Event.objects.create (event_title = event_title, event_description = event_description , event_date = event_date, event_time = event_time, event_address = event_address, event_capacity = event_capacity, event_price = event_price )
            #test = Event.objects.create()
            new_event.save()
            return HttpResponse ("New event is created and saved in database")
    
    return render (request, 'event_create_form.html', {'form': form})





@group_required('User')
#@authenticated_user
@login_required(login_url="/sign_in")
def purchase_ticket(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    user = request.user
    if request.method == "POST":
        form = TicketPurchaseForm(request.POST, initial={'event': event})
        if form.is_valid():
            #event = form.cleaned_data['event']
            ticket_quantity = form.cleaned_data['ticket_quantity']
            ticket_type = form.cleaned_data['ticket_type']
            
            if event.event_capacity >= ticket_quantity:
                total_price = event.event_price * ticket_quantity
            
            # create new ticket record
            ticket = Ticket.objects.create(
                event_details=event,
                user_details= user,
                ticket_quantity=ticket_quantity,
                total_price=total_price,
                status=ticket_type,
            )

            event.event_capacity -= ticket_quantity
            event.save()

            return HttpResponse(f'{ticket_quantity} Tickets has been placed of price {total_price} of event {event}.') 
        
         
    else:
        # Prepopulate the event in the form and make it non-editable
        form = TicketPurchaseForm(initial={'event': event})

    return render(request, 'purchase_ticket.html', {'form': form, 'event': event, 'user': user})

#@group_required('Admin')
#@login_required(login_url="/sign_in")
def ticket_details(request, user_id):
   # event = get_object_or_404(Event, id=event_id)
    user = get_object_or_404 (User, id=user_id)
    tickets = Ticket.objects.filter(user_details=user)
    #if request.method == 'POST':
    return render (request, 'ticket_details.html', {'user': user, 'tickets': tickets})



   

@login_required(login_url="/sign_in")
def index(request):
    if not request.user.is_authenticated:
        return redirect('sign_in')
    return render (request, 'index.html' )

# View for profile page
def profile(request):
    return render(request, 'profile.html')

# View for sign-up page
def sign_up(request):
    if request.method == 'POST':
        form = SignUpForm (request.POST)
        if form.is_valid():
            form.save()
            return redirect('ticket_app:sign_in')
        else:
            print(form.errors)
            messages.error(request, "There was an error creating your account.")
    else:
        form = SignUpForm()

    return render (request, 'sign_up.html', {'form':form} )   

# View for sign-in page
def sign_in(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
            # set user-specific data in the session
                request.session['username'] = username
                request.session.save()
                print("Session ID before logout:", request.session.session_key)
                if user.is_superuser:  
                    return redirect('admin_app:admin_home')
                return redirect('ticket_app:user_dashboard')
        else:
            print(form.errors)
               

            
    else:
        form = AuthenticationForm()
    return render(request, 'sign_in.html')


def add_event(request):
    if request.method == "POST":
        form = EventCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ticket_app:event_list')
    else:
        form = EventCreateForm()
    return render(request, 'add_event.html', {'form': form})


def delete_event(request, id):
    event = get_object_or_404(Event, id=id)
    if request.method == "POST":
        event.delete()
        return redirect('ticket_app:event_list')

def user_dashboard(request):
    
    return render (request, 'user_dashboard.html')

def user_ticket(request):
    
    ticket = Ticket.objects.filter(user_details=request.user)
    

    return render(request, 'user_ticket.html', {'ticket': ticket})
