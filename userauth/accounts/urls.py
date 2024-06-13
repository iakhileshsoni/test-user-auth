
from django.urls import path
from . import views

urlpatterns = [
    path('register', views.registration, name="register"),
    path('login', views.LoginView, name="login"),
    path('password-reset', views.password_reset, name="password_reset"),
    path('', views.home, name="home"),
]
