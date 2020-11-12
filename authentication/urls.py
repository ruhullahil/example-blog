from django.urls import path
from authentication.views import  register
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view() ,name = 'login'),
    path('logout/', auth_views.LogoutView.as_view() ,name = 'logout'),


    path('register/', register,name = 'register'),
]
