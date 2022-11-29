from django.shortcuts import render

from apps.news.models import News

from apps.contacts.models import Contact

from apps.settings.models import Setting
# Create your views here.

def news(request):
    new = News.objects.all()
    contact = Contact.objects.latest('id')
    setting = Setting.objects.latest('id')

    context = {
        'new':new,
        'contact':contact,
        'setting':setting
    }

    return render(request, 'blog.html', context)