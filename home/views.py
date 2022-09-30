from django.shortcuts import render
from django.http import JsonResponse
from django.template.loader import render_to_string

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


# ----- Cart ajax functions  

def add_to_cart(request):
	#del request.session['cartdata']
	cart_p = {}
	cart_p[str(request.GET['id'])] = {
		'image': request.GET['image'],
	    'title': request.GET['title'],
	    'qty': request.GET['qty'],
	    'price': request.GET['qty'],

	}
	if 'cartdata' in request.session:
		if str(request.GET['id']) in request.session['cartdata']:
			cart_data = request.session['cartdata']
			cart_data[str(request.GET['id'])]['qty']=int(cart_p[str(request.GET['id'])]['qty'])
			cart_data.update(cart_data)
			request.session['cartdata']=cart_data
		else:
		    cart_data=request.session['cartdata']
		    cart_data.update(cart_p)
		    request.session['cartdata']=cart_data	
	else:
	    request.session['cartdata']=cart_p	

	return JsonResponse({'data':request.session['cartdata'], 'totalitems': len(request.session['cartdata'])})


def cart(request):
	total_amt = 0
	for p_id, item in request.session['cartdata'].items():
		total_amt+=int(item['qty'])*float(item['price'])
	return render(request, 'home/carrinho.html', {'cart_data':request.session['cartdata'], 'totalitems': 
		len(request.session['cartdata']), 'total_amt': total_amt})


def delete_cart_item(request):
    p_id =str(request.GET['id'])
    if 'cartdata' in request.session:
        if p_id in request.session['cartdata']:
        	cart_data=request.session['cartdata']
        	del request.session['cartdata'][p_id]
        	request.session['cartdata']=cart_data
    total_amt=0
    for p_id,item in request.session['cartdata'].items():
    	total_amt+=int(item['qty'])*float(item['price'])
    t=render_to_string('home/includes/_cart-ajax.html', {'cart_data': request.session['cartdata'], 'totalitems': len(
    request.session['cartdata']), 'total_amt': total_amt})

    return JsonResponse({'data': t, 'totalitems':len(request.session['cartdata'])})	
            	


def update_to_cart(request):
    pass             	