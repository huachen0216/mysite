from django.shortcuts import render
from contact.forms import ContactForm
from django.core.mail import send_mail
from django.http import HttpResponseRedirect

def contact(request):
#     errors = []
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            send_mail(
                cd['subject'],
                cd['message'],
                cd.get('email', 'noreply@example.com'), 
                ['siteowner@example.com'],
            )
#                 ['siteowner@example.com'],
#             )
            return HttpResponseRedirect('/thanks/')
    else:
        form = ContactForm(
            initial={'subject': 'I love your site!'}
        )
    return render(request, 'contact_form.html', {'form':    form})
#             #         if not request.POST.get('subject', ''):
#             errors.append('Enter a subject.')
#         if not request.POST.get('message', ''):
#             errors.append('Enter a message.')
#         if request.POST.get('email') and '@' not in request.POST['email']:
#             errors.append('Enter a valid e-mail address.')
#         if not errors:
#             send_mail(
#                 cd['subject'],
#                 cd['message'], '1593555048@qq.com',
#                 [cd.get('email')], '1593555048@qq.com')
#             return HttpResponseRedirect('/thanks/')
#     else:
#         form = ContactForm()
#     return render(request, 'contact_form.html', {'form': form})
#     return render(request, 'contact_form.html', {
#         'errors': errors,
#         'subject': request.POST.get('subject', ''),
#         'message': request.POST.get('message', ''),
#         'email': request.POST.get('email', ''),
#     })

def thanks(request):
    return render(request, 'thanks.html')
