from django.contrib.auth.models import Group

def admin_context(request):
    if request.user.is_authenticated:
        user_groups = request.user.groups.values_list('name', flat=True) 
        is_admin = 'Admin' in user_groups
        is_user = 'User' in user_groups
    else:
        is_admin = False
        is_user = False
    
    return {
        'is_admin': is_admin,
        'is_user' : is_user,
    }