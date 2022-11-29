from django.shortcuts import render,redirect

from apps.news.models import News, Comment

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



def news_detail(request,id):

    new = News.objects.get(id =id)
    setting = Setting.objects.latest('id')
    contact = Contact.objects.latest('id')
    random_new = News.objects.all().order_by('?')
    if request.method == "POST":
        if 'comment' in request.POST:
                text = request.POST.get('text')
                comment = Comment.objects.create(user = request.user, post = new, text = text)
                return redirect('news_detail', new.id)

    context = {
        'setting':setting,
        'contact': contact,
        'new':new,
        'random_new':random_new,

    }

    return render(request, 'blog-details.html',context)