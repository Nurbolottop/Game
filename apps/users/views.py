from django.shortcuts import render,redirect

from django.contrib.auth import authenticate, login



from apps.settings.models import Setting
from apps.users.models import User
# Create your views here.
def user_login(request):
    setting = Setting.objects.latest('id')

    context ={
        'setting':setting
    }

    return render(request,'login.html',context)

def register(request):
    setting = Setting.objects.latest('id')
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        if password == confirm_password:
            user = User.objects.create(username = username, email = email)
            user.set_password(password)
            user.save()
            user = User.objects.get(username = username)
            user = authenticate(username = username, password = password)
            login(request , user)
            return redirect('index')
    context = {
        'setting' : setting,
    }

    return render(request,'signup.html',context)
