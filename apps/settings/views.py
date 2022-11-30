from django.shortcuts import render


from apps.settings.models import Setting,Data,Achievement,Game

from apps.contacts.models import Contact
from apps.news.models import News


# Create your views here.

def index(request):
    new = News.objects.all()


    setting = Setting.objects.latest('id')
    data = Data.objects.latest('id')
    achievement = Achievement.objects.latest('id')
    game = Game.objects.all()
    contact = Contact.objects.latest('id')
    
    context = {
        'setting':setting,
        'data':data,
        'achievement':achievement,
        'game':game,
        'contact':contact,
        'new':new,




    }

    return render(request, 'index.html', context)



def game(request):
    setting = Setting.objects.latest('id')
    game = Game.objects.all()
    contact = Contact.objects.latest('id')

    context = {
        'game':game,
        'setting':setting,
        'contact':contact,

    }

    return render(request, 'games.html', context)



def game_detail(request,id):
    game_detail = Game.objects.get(id = id)
    setting = Setting.objects.latest('id')
    contact = Contact.objects.latest('id')

    context = {
        'setting':setting,
        'contact':contact,

        'game_detail':game_detail
    }
    return render(request, 'games-details.html',context)
