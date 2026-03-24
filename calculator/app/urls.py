from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('calculator/', views.CalculatorView.as_view(), name='calculator'),
]