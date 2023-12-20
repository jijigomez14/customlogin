# urls.py
from django.urls import path
from .views import custom_login, custom_logout, home_view

urlpatterns = [
    path('login/', custom_login, name='custom_login'),
    path('logout/', custom_logout, name='custom_logout'),
    path('home/', home_view, name='home'),
]
