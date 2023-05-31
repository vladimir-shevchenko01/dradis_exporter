from django.contrib import admin
from django.urls import path

from auth_page import views

app_name = 'login'

urlpatterns = [
    path('', views.form_page, name='form_page'),
    path('login', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]
