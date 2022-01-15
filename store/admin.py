from django.contrib import admin
<<<<<<< HEAD
from .models import Product
=======
from .models import Product,Variation
>>>>>>> second commit

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
	list_display=('product_name','price','stock','catagory','modified_date','is_available')
	prepopulated_fields={'slug':('product_name',)}

admin.site.register(Product,ProductAdmin)
<<<<<<< HEAD
=======

class VarationAdmin(admin.ModelAdmin):
	list_display=('product','varation_category','varation_value','is_active')
	list_editable =('is_active',)
	list_filter = ('product','varation_category','varation_value')

admin.site.register(Variation,VarationAdmin)
>>>>>>> second commit
