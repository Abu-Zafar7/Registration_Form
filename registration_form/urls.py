from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.homepage,name="homepage"),
    path('homepage/',views.homepage,name="homepage"),
    path('signup/',views.signup, name="signup"),
    path('loginuser/',views.loginuser, name="loginuser"),
    path('logoutuser/',views.logoutuser, name="logoutuser")
]