from django.urls import path
from . import views

app_name = 'contas_basicas'

urlpatterns = [
    path('', views.home, name='home'),
]