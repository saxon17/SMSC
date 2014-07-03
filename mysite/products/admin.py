from django.contrib import admin
from models import Product
from models import SignUp
# Register your models here.
class ProductAdmin(admin.ModelAdmin):
	class Meta:
		model = Product	

admin.site.register(Product,ProductAdmin)


'''class SignUpAdmin(admin.ModelAdmin):
	class Meta:
		model = SignUp	
	

admin.site.register(SignUp,SignUpAdmin)
'''