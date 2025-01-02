from django.http import HttpResponseForbidden
from django.shortcuts import redirect

def authenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('ticket_app:login')
        
        return view_func (request, *args, **kwargs) # Allow access to the view if authenticated
    
    
    return wrapper_func

def group_required(*group_name, login_url="/sign_in"):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
            print(f"Dec User: {request.user}, Groups: {request.user.groups.values_list('name', flat=True)}")
    
            if not request.user.is_authenticated:
                return redirect(login_url)  # Redirect to login if not authenticated
            if not request.user.groups.filter(name__in=group_name).exists():
                return HttpResponseForbidden("You do not have permission to access this page.")
            return view_func(request, *args, **kwargs)
        return wrapper_func
    return decorator

