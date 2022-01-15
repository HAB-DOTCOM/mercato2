from django.shortcuts import render,redirect,get_object_or_404
from store.models import Product,Variation
from .models import Cart,CartItem
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.utils.datastructures import MultiValueDictKeyError
# Create your views here.
def _cart_id(request):
	cart = request.session.session_key
	if not cart:
		cart = request.session.create()
	return cart

def add_cart(request,product_id):
	product = Product.objects.get(id=product_id)
	product_varation=[]
	if request.method == 'POST':
		for item in request.POST:
			key = item
			value = request.POST[key]
			#print(key,value)
			try:
				varation = Variation.objects.get(product=product,varation_category__iexact=key,varation_value__iexact=value)
				product_varation.append(varation)
			except:
				pass
		
	try:
		cart = Cart.objects.get(cart_id = _cart_id(request))
	except Cart.DoesNotExist:
		cart = Cart.objects.create(
			cart_id = _cart_id(request)
		)
	cart.save()

	is_cart_item_exsits = CartItem.objects.filter(product=product,cart=cart).exists()


	if is_cart_item_exsits:
		cart_item = CartItem.objects.filter(product=product,cart=cart)
		#exsisting varation
		#curent varation
		#cart_item id
		ex_var_list=[]
		id = []
		for item in cart_item:
			exsisting_varation = item.varations.all()
			ex_var_list.append(list(exsisting_varation))
			id.append(item.id)
			if product_varation in ex_var_list:
				#return HttpResponse('true')
				index = ex_var_list.index(product_varation)
				item_id = id[index]
				item = CartItem.objects.get(product=product,id=item_id)
				item.quantity +=1
				item.save()

			else:
				item = CartItem.objects.create(product=product,quantity=1,cart=cart)
				#return HttpResponse('flase')
				if len(product_varation)> 0:
					item.varations.clear()	
					item.varations.add(*product_varation)
				item.save()
	else :
		cart_item = CartItem.objects.create(
			product=product,
			quantity=1,
			cart=cart,
		)
		if len(product_varation)> 0:
			cart_item.varations.clear()
			cart_item.varations.add(*product_varation)
		
		cart_item.save()
	return redirect('cart')

def remove_cart(request,product_id,cart_item_id):
	cart=Cart.objects.get(cart_id=_cart_id(request))
	product= get_object_or_404(Product,id=product_id)
	try:
		cart_item = CartItem.objects.get(cart=cart,product=product,id=cart_item_id)
		if cart_item.quantity > 1:
			cart_item.quantity -=1
			cart_item.save()
		else:
			cart_item.delete()
	except:
		pass
	return redirect('cart')

def remove_cart_item(request,product_id,cart_item_id):
	cart= Cart.objects.get(cart_id=_cart_id(request))
	product = get_object_or_404(Product,id=product_id)
	cart_item = CartItem.objects.get(cart=cart,product=product,id =cart_item_id)
	cart_item.delete()
	return redirect('cart')

def cart(request, total=0,quantity=0,cart_items=None):
	tax=0
	grand_total=0
	try:
		cart = Cart.objects.get(cart_id=_cart_id(request))
		cart_items = CartItem.objects.filter(cart=cart,is_active=True)
		for cart_item in cart_items:
			total += (cart_item.product.price * cart_item.quantity)
			quantity += cart_item.quantity
		tax= (2*total)/100
		grand_total= total + tax
	except ObjectDoesNotExist:
		pass
	context = {
		'total':total,
		'quantity':quantity,
		'cart_items':cart_items,
		'tax':tax,
		'grand_total': grand_total,
	}
	return render(request,'store/cart.html',context)
