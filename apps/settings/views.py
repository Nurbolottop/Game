from django.shortcuts import render


from apps.settings.models import Setting,Data,Achievement,Game



# Create your views here.

def index(request):

    setting = Setting.objects.latest('id')
    data = Data.objects.latest('id')
    achievement = Achievement.objects.latest('id')
    game = Game.objects.all()
    
    context = {
        'setting':setting,
        'data':data,
        'achievement':achievement,
        'game':game,


    }

    return render(request, 'index.html', context)



def game(request):
    setting = Setting.objects.latest('id')
    game = Game.objects.all()

    context = {
        'game':game,
        'setting':setting,
    }

    return render(request, 'games.html', context)



def game_detail(request,id):
    game_detail = Game.objects.get(id = id)
    setting = Setting.objects.latest('id')

    context = {
        'setting':setting,

        'game_detail':game_detail
    }
    return render(request, 'games-details.html',context)
