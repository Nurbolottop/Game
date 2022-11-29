"""Games URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth.views import LogoutView

from apps.users.views import register,user_login,register_eror,login_eror

from apps.about.views import about

from apps.teams.views import teams

from apps.faq.views import faq

from apps.contacts.views import contact

from apps.news.views import news


from apps.settings.views import index,game_detail,game


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name="index"),
    path('game_detail/<int:id>/', game_detail, name="game_detail"),
    path('register/', register, name = "register"),
    path('login/', user_login, name = "login"),
    path('logout/',LogoutView.as_view(next_page = "index"), name="logout"),
    path('register_eror', register_eror, name = "register_eror"),
    path('login_eror/', login_eror, name = "login_eror"),
    path('game/', game, name = "game"),
    path('about/', about, name = "about"),
    path('teams/', teams, name = "teams"),
    path('faq/', faq, name = "faq"),
    path('contact/', contact, name = "contact"),
    path('news/', news, name = "news"),







]
urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)