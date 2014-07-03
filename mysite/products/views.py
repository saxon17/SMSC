from django.shortcuts import render,render_to_response,RequestContext

# Create your views here.

from products.forms import ProductForm

def product_add(request):



	form = ProductForm()
	return render_to_response("Product.html",
		locals(),RequestContext(request))
