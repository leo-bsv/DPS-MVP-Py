from django.urls import path, include

from . import views

urlpatterns = [
    path(
        '', views.home, name='home'
    ),
    path('add_company', views.add_company, name='company')
]