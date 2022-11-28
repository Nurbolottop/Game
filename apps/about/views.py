from django.shortcuts import render

from apps.about.models import About
from apps.settings.models import Setting,Achievement
# Create your views here.

def about(request):
    setting = Setting.objects.latest('id')
    about = About.objects.latest('id')
    achievement = Achievement.objects.latest('id')

    context = {
        'setting':setting,
        'about':about,
        'achievement':achievement,

    }

    return render(request, 'about.html',context)