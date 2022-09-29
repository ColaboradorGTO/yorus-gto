from django.shortcuts import render

# My Model Product 
from product . models import *

# Create your views here.

def index(request):
	brand = Brand.objects.all()
	category = Category.objects.all().order_by('-created')[0:4]
	product = Product.objects.all()

	context = {
		'brand_list': brand,
	    'product_list': product,
	    'category_list': category,
	}
	
	return render(request, 'home/index.html', context)


def header(request):
	category = Category.objects.all()

	context = {
		'category_list': category, 
	}
	return render(request,  'home/includes/header.html', context)


def product_details(request, pk):
	product = Product.objects.all()
	product_detail = Product.objects.get(id=pk)

	context = {
	    'product_detail': product_detail,
	    'product_list': product,
	}



	return render(request, 'home/detalhes-do-produto.html', context)	