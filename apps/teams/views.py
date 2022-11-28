from django.shortcuts import render

from apps.teams.models import Teams
from apps.settings.models import Setting

# Create your views here.
def teams(request):
    team = Teams.objects.all()
    setting = Setting.objects.latest('id')

    context = {
        'team':team,
        'setting':setting
    }

    return render(request, 'team.html', context)