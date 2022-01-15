from django.urls import path
from .models import Product
from . import views

urlpatterns = [
    
    path('',views.store,name='store'),
<<<<<<< HEAD
    path('<slug:catagory_slug>/',views.store,name='product_by_catagory'),
    path('<slug:catagory_slug>/<slug:product_slug>/',views.product_detial,name='product_detial'),
=======
    path('catagory/<slug:catagory_slug>/',views.store,name='product_by_catagory'),
    path('catagory/<slug:catagory_slug>/<slug:product_slug>/',views.product_detial,name='product_detial'),
    path('search/',views.search,name='search'),
>>>>>>> second commit
    
]
#+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
