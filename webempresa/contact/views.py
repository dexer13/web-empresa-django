from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.mail import EmailMessage
from .forms import ContactForm
def contact(request):
    form = ContactForm()
    if request.POST:
        print('entro al post')
        form=ContactForm(data=request.POST)
        if form.is_valid():
            name=request.POST.get('name', '')
            email=request.POST.get('email', '')
            content=request.POST.get('content', '')
            email=EmailMessage(
                "LA CAFETERIA",
                "De {}<{}>\n\nEsribió\n{}".format(name, email, content),
                "no_contestar_este_correo@inbox.emailtrap.io",
                ['xer131@hotmail.com'],
                reply_to=[email]
            )
            try:
                email.send()
            except:
                #Algo salió mal
                return redirect(reverse('contact:contact')+'?fail')
            return redirect(reverse('contact:contact')+'?ok')
    else:
        print('no entró al post')
    return render(request, 'contact/contact.html', {'form':form})
# Create your views here.
