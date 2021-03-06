from django.conf.urls import patterns, include, url
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'testproject.views.home', name='home'),
    # url(r'^testproject/', include('testproject.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^books/$', 'books.views.index'),
    url(r'^add/$', 'books.views.add_from_form'),
    url(r'^delete/$', 'books.views.delete_from_form'),
    url(r'^update/$', 'books.views.update_from_form'),
    url(r'^search/$', 'books.views.search_from_form'),
    url(r'^search_isbn/$', 'books.views.search_isbn_from_form'),
    
  )
