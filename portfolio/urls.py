from django.urls import path
from . import views


urlpatterns = [
    path('', views.home_page),
    path('get-ip-data', views.get_ip_data),
]
