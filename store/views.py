from django.shortcuts import render,get_object_or_404
from .models import *
from catagory.models import catagory
<<<<<<< HEAD
=======
from carts.models import CartItem
from carts.views import _cart_id
from django.core.paginator import EmptyPage,PageNotAnInteger,Paginator
from django.db.models import Q
>>>>>>> second commit

# Create your views here.

def store(request,catagory_slug=None):
	categories=None
	products=None

	if catagory_slug!= None:
		categories=get_object_or_404(catagory,slug=catagory_slug)
		products=Product.objects.filter(catagory=categories,is_available=True)
<<<<<<< HEAD
		product_count=products.count()
	else:
		products=Product.objects.all().filter(is_available=True)
		product_count =products.count()

	context={
		'products':products,
=======
		paginator = Paginator(products, 3)
		page_number = request.GET.get('page')
		page_obj = paginator.get_page(page_number)
		product_count=products.count()
	else:
		products=Product.objects.all().filter(is_available=True).order_by('id')
		paginator = Paginator(products, 2)
		page_number = request.GET.get('page')
		page_obj = paginator.get_page(page_number)
		product_count =products.count()

	context={
		'products':page_obj,
>>>>>>> second commit
		'product_count':product_count,

	}
	return render(request,'store/store.html',context)

def product_detial(request,catagory_slug,product_slug):
	try:
		single_product=Product.objects.get(catagory__slug=catagory_slug,slug=product_slug)
<<<<<<< HEAD
=======
		in_cart=CartItem.objects.filter(cart__cart_id=_cart_id(request),product=single_product).exists()

>>>>>>> second commit
	except Exception as e:
		raise e
	context={
		'single_product':single_product,
<<<<<<< HEAD
	}
	return render(request,'store/product_detial.html',context)

=======
		'in_cart'		:in_cart,
	}
	return render(request,'store/product_detial.html',context)

def search(request):
	if 'keyword'in request.GET:
		keyword = request.GET['keyword']
		if keyword:
			products = Product.objects.order_by('-created_date').filter(Q(description__icontains=keyword) |Q(product_name__icontains=keyword))
			product_count =products.count()
	context ={
		'products':products,
		'product_count':product_count,
		'keyword':keyword,

	}

	return render(request,'store/store.html',context)

>>>>>>> second commit
