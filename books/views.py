<<<<<<< HEAD
from django.shortcuts import render

# Create your views here.
=======
# from django.shortcuts import render_to_reponse

from django.shortcuts import render_to_response

def search_form(request):
    return render_to_response('search_form.html')
>>>>>>> refs/heads/dev_thinkpad
