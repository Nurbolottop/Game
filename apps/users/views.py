from django.shortcuts import render,redirect



from django.contrib.auth import authenticate, login



from apps.settings.models import Setting
from apps.users.models import User
# Create your views here.
def user_login(request):
    setting = Setting.objects.latest('id')
    if request.method =="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user = User.objects.get(username = username)
            user = authenticate(username=username, password=password)
            login(request,user)
            return redirect('index')
        except:
            return redirect('login_eror')
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
            if username and email and password and confirm_password:
                try:
                    user = User.objects.create(username = username, email = email)
                    user.set_password(password)
                    user.save()
                    user = User.objects.get(username = username)
                    user = authenticate(username = username, password = password)
                    login(request, user)
                    return redirect('index')
                except:
                    return redirect('register_eror')
            else:
                return redirect('register_eror')
        else:
            return redirect('register_eror')
    context = {
        'setting' : setting,
    }

    return render(request,'signup.html',context)

def register_eror(request):
    context = {}
    return render(request, 'register_eror.html', context)

def login_eror(request):
    context = {}
    return render(request, 'login_eror.html', context)