from django.conf.urls import *
# from mysite.views import hello, current_datetime, hours_ahead
# from mysite import views
from django.contrib import admin
# from books.views import *
# from contact.views import *
from django.conf import settings
from mysite import views


admin.autodiscover()

urlpatterns = patterns('mysite.views',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    (r'^hello/$', 'hello'),
    (r'^time/$', 'current_datetime'),
    (r'^time/plus/(\d{1,2})/$', 'hours_ahead'),
#     (r'^foo/$', views.foobar_views, {'template_name': 'template1.html'}),
#     (r'^bar/$', views.foobar_views, {'template_name': 'template2.html'}),
#     (r'^events/$', views.event_list, {'model': models.Event}),
#     (r'^blog/entries/$', views.entry_list, {'model': models.BlogEntry}),
#     (r'^blog/$', views.page),
#     (r'^blog/page(?P<num>\d+)/$', views.page),
#     ('^([^/]+)/([^/]+)/add/$', views.add_stage),
    (r'^articles/(\d{4})/(\d{2})/(\d{2})/$', views.day_archive),
#     (r'^somepage/$', views.some_page),
    (r'^somepage/$', views.method_splitter, {'GET': views.some_page_get, 'POST': views.some_page_post}),
)

urlpatterns += patterns('books.views',
    (r'^search-form/$', 'search_form'),
    (r'^search/$', 'search'),                   
)
    
urlpatterns += patterns('contact.views',
    (r'^contact/$', 'contact'),
    (r'^thanks/$', 'thanks'),                     
)    
      
urlpatterns += patterns('',

#     (r'^foo/$', views.foo_view),
#     (r'^bar/$', views.bar_view),
#     (r'^$', views.hompage),
#     (r'^(\d{4})/([a-z]{3})', views.archive_month),                    
)

# if settings.DEBUG:
#     urlpatterns += patterns('',
#         (r'^debuginfo/$', views.debug),
# )
