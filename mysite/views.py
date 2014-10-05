#from django.template.loader import get_template
#from django.template import Context
from django.shortcuts import render_to_response
from django.http import Http404, HttpResponse
import datetime

def hello(request):
    return HttpResponse("Hello world")

def current_datetime(request):
    #now = datetime.datetime.now()
    #return render_to_response('current_datetime.html', {'current_date': now})
    #t = get_template('current_datetime.html')
    #html = t.render(Context({'current_date': now}))
    #return HttpResponse(html)
    current_date = datetime.datetime.now()
    return render_to_response('dateapp/current_datetime.html', locals())

def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    html = "<html><body>In %s hour(s), it will be %s.</body></html>" % (offset, dt)
    return HttpResponse(html)
