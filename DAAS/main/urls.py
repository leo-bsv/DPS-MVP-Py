from django.urls import path, include

from . import views

urlpatterns = [
    path(
        '', views.home, name='home'
    ),
    path('add_company', views.add_company, name='company'),
    path('company_list', views.comp_list, name='company_list'),
    path('models', views.models_s, name='models'),
    path('orders', views.orders_view, name='orders'),
]