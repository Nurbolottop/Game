from django.shortcuts import render

from apps.teams.models import Teams
from apps.settings.models import Setting
from apps.contacts.models import Contact

# Create your views here.
def teams(request):
    team = Teams.objects.all()
    setting = Setting.objects.latest('id')
    contact = Contact.objects.latest('id')

    context = {
        'team':team,
        'setting':setting,
        'contact':contact,

    }

    return render(request, 'team.html', context)