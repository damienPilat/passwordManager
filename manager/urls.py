from django.urls import path
from . import views

app_name = 'manager'
urlpatterns = [
    path('', views.login, name='login'),
    path('login_check/', views.login_check, name='login_check'),
    path('reset_password/', views.reset_password, name='reset_password'),
    path('signup/', views.signup, name='signup'),
    path('main/', views.main, name='main'),
    path('profile/', views.profile, name='profile'),
    path('settings/', views.settings, name='settings'),
    path('about/', views.about, name='about'),
]
