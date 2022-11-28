from django.shortcuts import render

from apps.faq.models import Faq

from apps.settings.models import Setting
# Create your views here.

def faq(request):
    setting  = Setting.objects.latest('id')
    faq = Faq.objects.all()

    context = {
        'setting':setting,
        'faq':faq
    }

    return render(request, 'faq.html', context)