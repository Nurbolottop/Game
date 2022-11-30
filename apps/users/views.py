from django.shortcuts import render,redirect



from django.contrib.auth import authenticate, login



from apps.settings.models import Setting
from apps.users.models import User
from apps.contacts.models import Contact

# Create your views here.
def user_login(request):
    setting = Setting.objects.latest('id')
    contact = Contact.objects.latest('id')

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
        'setting':setting,
        'contact':contact,

    }

    return render(request,'login.html',context)

def register(request):
    setting = Setting.objects.latest('id')
    contact = Contact.objects.latest('id')

    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        profile_image = request.FILES.get('profile_image')

        if password == confirm_password:
            if username and email and password and confirm_password:
                try:
                    user = User.objects.create(username = username, email = email,profile_image = profile_image)
                    user.set_password(password)
                    user.save()
                    user = User.objects.get(username = username)
                    user = authenticate(username = username, password = password)
                    login(request, user)
                    return redirect('index')
                except:
                    return redirect('register_eror')
            else:
                return redirect('register_not_null_eror')
        else:
            return redirect('register_password_eror')
    context = {
        'setting' : setting,
        'contact':contact,

    }

    return render(request,'signup.html',context)

def register_eror(request):
    setting = Setting.objects.latest('id')

    context = {
        'setting' : setting
    }
    return render(request, 'register_eror.html', context)

def register_not_null_eror(request):
    setting = Setting.objects.latest('id')

    context = {
        'setting' : setting
    }
    return render(request, 'register_not_null_eror.html', context)

def register_password_eror(request):
    setting = Setting.objects.latest('id')

    context = {
        'setting' : setting
    }
    return render(request, 'register_password_eror.html', context)


def login_eror(request):
    setting = Setting.objects.latest('id')

    context = {
        'setting' : setting
    }
    return render(request, 'login_eror.html', context)