#from django.template.loader import get_template
#from django.template import Context
from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect, HttpResponse
import datetime
# from mysite.models import Event, BlogEntry

def hello(request):
    return HttpResponse("Hello world")

def current_datetime(request):
    #now = datetime.datetime.now()
    #return render_to_response('current_datetime.html', {'current_date': now})
    #t = get_template('current_datetime.html')
    #html = t.render(Context({'current_date': now}))
    #return HttpResponse(html)
    current_date = datetime.datetime.now()
    return render(request, 'dateapp/current_datetime.html', locals())

def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    html = "<html><body>In %s hour(s), it will be %s.</body></html>" % (offset, dt)
    return HttpResponse(html)

# def foo_view(request):
#     m_list = MyModel.objects.filter(is_new=True)
#     return render(request, 'template1.html', {'m_list': m_list})
# 
# def bar_view(request):
#     m_list = MyModel.objects.filter(is_new=True)
#     return render(request, 'template2.html', {'m_list': m_list})

# def foobar_view(request, url):
#     m_list = MyModel.objects.filter(is_new=True)
#     if url == 'foo':
#         template_name = 'template1.html'
#     elif url == 'bar':
#         template_name = 'template2.html'
#     return render(request, template_name, {'m_list': m_list})

# def foobar_views(request, template_name):
#     m_list = MyModel.objects.filter(is_new=True)
#     return render(request, template_name, {'m_list': m_list})

# def event_list(request):
#     obj_list = Event.objects.all()
#     return render(request, 'mysite/event_list.html', {'event_list': obj_list})
#     
# def entry_list(request):
#     obj_list = BlogEntry.objects.all()
#     return render(request, 'mysite/blogentry_list.html', {'entry_list': obj_list})

# def object_list(request, models):
#     obj_list = models.objects.all()
#     template_name = 'mysite/%s_list.html' %models.__name__.lower()
#     return render(request, template_name, {'object_list': obj_list})


# def page(request, num='1'):
#     #
#     #


def day_archive(request, year, month, day):
#     date = datetime.datetime(int(year), int(month), int(day))
    date = datetime.datetime(year, month, day)

def method_splitter(request, GET=None, POST=None):
    if request.method == 'GET' and GET is not None:
        return GET(request)
    elif request.method == 'POST' and POST is not None:
        return POST(request)
    raise Http404
 
def some_page_get(request):
#     if request.method == 'POST':
#         do_something_for_post()
#         return HttpResponseRedirect('/someurl/')
#     elif request.method == 'GET':
#         do_something_for_get()
#         return render(request, 'page.html')
#     else:
#         raise Http404()
    assert request.method == 'GET'
    do_something_for_get()
    return render(request, 'page.html')

def some_page_post(request):
    assert request.method == 'POST'
    do_something_for_post()
    return HttpResponseRedirect('/someurl/')



    
    

    
    
    
    
    
    
    
    