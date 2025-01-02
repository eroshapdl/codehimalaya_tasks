"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from mysite import views
from django.conf.urls import include
from .views import MyFormView, HomeView, AboutUsView, CourseDetailsView, AddNumbersView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('about-us/', AboutUsView.as_view() ),
    path('', HomeView.as_view()),
    path('about-us/<str:courseid>', CourseDetailsView.as_view() ),
    path("yourname/", MyFormView.as_view(), name="yourname"),    
    path('add_numbers/', AddNumbersView.as_view()),
    path ('create_student/', views.create_student),
   


]
