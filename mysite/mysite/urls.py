from django.conf.urls import patterns, include, url
from views import current_datetime,hello,hours_ahead
from django.contrib import admin
admin.autodiscover()
from django.conf import settings
from django.conf.urls.static import static
from products.views import product_add
#urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    	
#    url(r'^admin/', include(admin.site.urls)),
#)



urlpatterns = patterns('',
     (r'^hello/$',hello),
     (r'^product_add/$',product_add),
     (r'^time/$',current_datetime),
     (r'^time/plus/(\d{1,2})/$',hours_ahead),
     url(r'^admin/', include(admin.site.urls)),
)
'''
if settings.DEBUG:
	urlpatterns = patterns('',
	    # ... the rest of your URLconf goes here ...
	) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

	urlpatterns = patterns('',
	    # ... the rest of your URLconf goes here ...
	) + static(settings.MEDIA_URL, document_root=settings.STATIC_ROOT)

'''
if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, 
		document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, 
		document_root=settings.MEDIA_ROOT)

