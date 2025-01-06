from django.urls import path
from . import views



app_name = 'admin_app'  

urlpatterns = [
    path('', views.admin_home, name='admin_home'),
   # path('sign_in/', views.sign_in, name='sign_in'),
    path("dashboard/", views.admin_dashboard, name="admin_dashboard"),
    path('user_list/', views.user_list, name='user_list'),
    path('user_list/<int:id>/', views.detail_view, name='user_detail' ),
    path('users/add/', views.add_user, name='add_user'),
    path('users/<int:id>/delete', views.delete_user, name='delete_user'),
    path('ticket_sales/<int:id>/', views.ticket_sales, name='ticket_sales'),
    path('event_list_ticket/', views.event_list_ticket, name='event_list_ticket'),
    
]

   
