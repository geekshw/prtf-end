from django.urls import path
from .views import index
# project/urls.py

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.base.urls')),
]

urlpatterns = [
    path('', index, name="index")
]