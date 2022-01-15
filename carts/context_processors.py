from .models import Cart,CartItem
from .views import _cart_id

def counter(request):
	cart_count = 0
	if 'admin' in request.path:
		return{}
	else:
		try:
			cart = Cart.objects.filter(cart_id=_cart_id(request))
			cart_itmes = CartItem.objects.all().filter(cart=cart[:1])
			for cart_itme in cart_itmes:
				cart_count += cart_itme.quantity
		except Cart.DoesNotExist:
			cart_count= 0
	return dict(cart_count=cart_count)