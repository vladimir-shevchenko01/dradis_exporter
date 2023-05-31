from django.urls import path

from parse import views

app_name = 'parse'

urlpatterns = [
    path('parse/', views.parse_html_view, name='parse'),
]