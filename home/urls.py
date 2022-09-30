from django.urls import path

# My Views 
from . import views


urlpatterns = [
	
	# Pages home
    path('', views.index, name='index'),
    path('detalhes-do-produto/<int:pk>/', views.product_details, name='detalhes-do-produto'),
    path('carrinho/', views.cart, name='carrinho'), 

    # Cart ajax 
    path('add-to-cart', views.add_to_cart, name='add-to-cart'), 
    path('delete-cart-item', views.delete_cart_item, name='delete-cart-item'), 
    path('update-to-cart', views.update_to_cart, name='update-to-cart'),
    

]
