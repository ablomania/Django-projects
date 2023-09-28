from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import articles, user,book

# Create your views here.

def homepage(request):
    myarticles = articles.objects.all().order_by('-date_posted')[:5]
    lastarticle = articles.objects.filter().last()
    template =  loader.get_template('index.html')
    context = {
        'article' : myarticles, 'lastitem' : lastarticle,
    }
    return HttpResponse(template.render(context, request))    

def mainpage(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render())


def read(request, id):
    template = loader.get_template('read.html')
    reader = articles.objects.get(id=id)
    lastarticle = articles.objects.filter().last()
    otherarticles = articles.objects.all().order_by('date_posted')
    if reader.id == lastarticle.id:
        readerf = 1
    else:
        readerf = reader.id +1
    if reader.id == 1:
        readerb = 1
    else:
        readerb = reader.id - 1

    context = {
        'reader' : reader, 'readerf': readerf, 'readerb': readerb, 'otherarticles': otherarticles,
    }
    reader = readerf
    return HttpResponse(template.render(context, request))



def createaccount(request):
    template = loader.get_template('account.html')
    context ={}
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        age = request.POST['age']
        email = request.POST['email']
        password = request.POST['password']
        passwordre = request.POST['password1']
        if len(password) < 8:
            template = loader.get_template('new_user.html')
            context = {'error': 'password is too short'}
            return HttpResponse(template.render(context, request))
        else:
            if password == passwordre:
                new_user = user(firstname=firstname, lastname=lastname, age=age, email=email, password=password)
                new_user.save()
            else:
                template = loader.get_template('new_user.html')
                context = {'error': 'password mismatch'}
                return HttpResponse(template.render(context, request))
    return HttpResponse(template.render(context, request))

def allarticles(request):
    marticles = articles.objects.all().order_by('-date_posted')
    template = loader.get_template('articlespage.html')
    context = {
        'myarticles' : marticles,
    }
    return HttpResponse(template.render(context, request))

def contact(request):
    template = loader.get_template('about.html')
    context = {
        'myname': 'Abel Amarteifio', 'myemail': 'abelamarteifio@gmail.com', 'mynumber' : '+233 59 877 9958'
    }
    return HttpResponse(template.render(context, request))

def details(request, id):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        myuser = user.objects.get(email=email)
        
        if len(password) < 8:
            template = loader.get_template('new_user.html')
            context = {'error': 'password is too short'}
            return HttpResponse(template.render(context, request))
        else:
            if password == myuser.password:
               myaccnt = user.objects.get(id=id)
               template = loader.get_template('details.html')
               context = {'myaccnt' : myaccnt,}
               return HttpResponse(template.render(context, request))
            else:
                template = loader.get_template('new_user.html')
                context = {'error': 'password mismatch'}
                return HttpResponse(template.render(context, request))
    myaccnt = user.objects.get(id=id)
    template = loader.get_template('details.html')
    context = {
        'myaccnt' : myaccnt,
    }
    return HttpResponse(template.render(context, request)) 