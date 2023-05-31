from django.contrib import admin
from django.urls import path

from save import views

app_name = 'save_doc'

urlpatterns = [
    path('save/', views.save_doc_view, name='save'),
]
