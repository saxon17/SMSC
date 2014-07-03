from django.template.loader import get_template
from django.template import Context
from django.http import Http404,HttpResponse
#from forms import ProductForm
def hello(request):
   return HttpResponse("Hello world")
import datetime

def current_datetime(request):
    now = datetime.datetime.now()
    t = get_template('current_datetime.html')
    html = t.render(Context({'current_date': now}))
    return HttpResponse(html)


def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
       raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    assert False
    html = "<html><body>In %s hour(s), it will be %s.</body></html>" % (offset, dt)
    return HttpResponse(html)





'''def product_add(request):
    
    form = ProductForm()
    return render_to_response("ProductForm.html",
        locals(),context_intance=RequestContext(request))
'''