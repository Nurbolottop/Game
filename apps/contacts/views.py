from django.shortcuts import render,redirect

from django.core.mail import send_mail

from apps.contacts.models import Contact,Contact_detail

from apps.settings.models import Setting

# Create your views here.

def contact(request):
    setting = Setting.objects.latest('id')
    contact = Contact.objects.latest('id')
    if request.method =="POST":
        name = request.POST.get('name')
        subject = request.POST.get('subject')
        email = request.POST.get('email')
        message = request.POST.get('message')
        Contact_detail.objects.create(name = name,email = email,message = message, subject = subject)
        send_mail(
            f'{subject}',
            f'{name} Здравствуйте, спасибо за отклик, мы с вами в скором времени свяжемся. Ваше сообщение: {message} Ваши контакты: {email}',
            "noreply@somehost.local",
            [email]
        )
        return redirect('index')
    context = {
        'setting':setting,
        'contact': contact
    }

    return render(request, 'contact.html', context)