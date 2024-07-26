from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    # You can add more URL patterns here for other views if needed
]
