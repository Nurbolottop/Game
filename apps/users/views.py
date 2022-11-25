from django.shortcuts import render

from apps.settings.models import Setting

# Create your views here.
def login(request):
    setting = Setting.objects.latest('id')

    context ={
        'setting':setting
    }

    return render(request,'login.html',context)

def register(request):
    setting = Setting.objects.latest('id')
    # if request.method == "POST":
    #     username = request.POST.get('username')
    #     email = request.POST.get('email')
    #     password = request.POST.get('password')
    #     confirm_password = request.POST.get('confirm_password')
    #     user = User.

    context ={
        'setting':setting
    }

    return render(request,'signup.html',context)
