from django.shortcuts import render
from yuekao import models as lapp
from django.http import HttpResponse


# Create your views here.

def regisets(request):
    return render(request, 'regiset.html')


def regiset(request):
    name = request.POST.get('name')
    pwd = request.POST.get('pwd')
    zhan = lapp.user.objects.all()
    for i in zhan:
        if i.uname == name:
            return HttpResponse('已被注册')
    a = lapp.user()
    a.uname = name
    a.upwd = pwd
    a.save()
    return render(request, 'login.html')


def login(request):
    return render(request, 'login.html')


def login_handle(request):
    username = request.POST.get('name')
    pwd = request.POST.get('pwd')
    str(username)
    str(pwd)
    try:
        a = lapp.user.objects.get(uname=username)
        if a.upwd == pwd:
            return render(request, 'index.html')

        else:
            return HttpResponse('密码错误')

    except:
        return HttpResponse('没有用户')

def index_handle(request):
    name = request.POST.get('name')
    email = request.POST.get('email')
    address = request.POST.get('address')
    text = request.POST.get('message')
    try:
        b = lapp.user.objects.get(uname=name)
        b.uname = name
        b.uemail = email
        b.uaddress = address
        b.utext = text
        b.save()
        c = lapp.user.objects.all()

        return render(request,'list.html',{'c':c})
    except:
        a = lapp.user()
        a.uname = name
        a.uemail = email
        a.uaddress = address
        a.utext = text
        a.save()
        return render(request, 'list.html')


