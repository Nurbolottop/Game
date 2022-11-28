from django.shortcuts import render

from apps.about.models import About

from apps.contacts.models import Contact

from apps.settings.models import Setting,Achievement


def about(request):
    setting = Setting.objects.latest('id')
    about = About.objects.latest('id')
    achievement = Achievement.objects.latest('id')
    contact = Contact.objects.latest('id')

    context = {
        'setting':setting,
        'about':about,
        'achievement':achievement,
        'contact':contact,


    }

    return render(request, 'about.html',context)
