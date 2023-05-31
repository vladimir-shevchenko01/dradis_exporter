from django.urls import path

from html_app import views

app_name = 'html_import'

urlpatterns = [
    path('import/', views.import_file_view, name='import'),
]

