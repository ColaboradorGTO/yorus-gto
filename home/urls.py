from django.urls import path

# My Views 
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('detalhes-do-produto/<int:pk>/', views.product_details, name='detalhes-do-produto'), 
]
