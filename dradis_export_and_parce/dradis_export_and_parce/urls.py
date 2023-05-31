from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('auth_page.urls')),
    path('html/', include('html_app.urls')),
    path('parse/', include('parse.urls')),
    path('save/', include('save.urls')),
    path('admin/', admin.site.urls),
]
