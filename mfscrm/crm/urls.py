

from django.conf.urls import url
from . import views
from django.urls import path, re_path

app_name = 'crm'
urlpatterns = [
    path('', views.home, name='home'),
    re_path(r'^home/$', views.home, name='home'),
    path('customer_list', views.customer_list, name='customer_list'),
    path('customer/<int:pk>/edit/', views.customer_edit, name='customer_edit'),
    path('customer/<int:pk>/delete/', views.customer_delete, name='customer_delete'),
]

