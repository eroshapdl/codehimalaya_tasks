from django.urls import path
from . import views


app_name = 'ticket_app'  

urlpatterns = [
    path('', views.index, name="index"),
    path('logout/', views.logout_view, name='logout'),
    path('events/', views.event_list, name='event_list'),
    path('event_view/<int:id>/', views.event_view, name='event_view'),
    path('event_create_form/', views.event_create_form, name='event_create_form'),
    path('purchase/<int:event_id>/', views.purchase_ticket, name='purchase_ticket'),
    path('profile/', views.profile, name='profile'),
    path('sign_up/', views.sign_up, name = 'sign_up'),
    path('sign_in/', views.sign_in, name = 'sign_in'),
    path('add_event/', views.add_event, name = 'add_event'),
    path('event_view/<int:id>/delete', views.delete_event, name='delete_event'),
    path('user_dashboard/', views.user_dashboard, name = 'user_dashboard'),
    path('ticket_details/<int:user_id>/', views.ticket_details, name='ticket_details'),
    path('user_ticket/', views.user_ticket, name='user_ticket'),
 
    
] 
