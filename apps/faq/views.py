from django.shortcuts import render

from apps.faq.models import Faq

from apps.contacts.models import Contact

from apps.settings.models import Setting
# Create your views here.

def faq(request):
    setting  = Setting.objects.latest('id')
    faq = Faq.objects.all()
    contact  = Contact.objects.latest('id')

    context = {
        'setting':setting,
        'faq':faq,
        'contact':contact,

    }

    return render(request, 'faq.html', context)