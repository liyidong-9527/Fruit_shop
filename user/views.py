from django.shortcuts import render, redirect
from .forms import UserModelForm
from .models import User, AddressInfo
import hashlib
from django.http import HttpResponse
import json


# Create your views here.


def reg(request):
    return render(request, "register.html")


def login(request):
    return render(request, "login.html")


def user_login(request):
    u = request.POST.dict()
    pwd = u["password"]
    # 密码加密
    m = hashlib.md5()
    m.update(pwd.encode())
    password = m.hexdigest()
    user = User.objects.filter(username=u["username"], password=password)
    if len(user) == 0:
        status = 500
    else:
        us = UserModelForm(instance=user[0])
        us.is_valid()
        user = us.initial
        request.session["user"] = user
        status = 200
    return HttpResponse(json.dumps({"status": status}))


def reg_user(request):
    u = UserModelForm(request.POST)
    pwd = u.cleaned_data["password"]
    # 密码加密
    m = hashlib.md5()
    m.update(pwd.encode())
    password = m.hexdigest()
    if u.is_valid():
        # 校验通过，获取实例对象，并修改password
        u.instance.password = password
        # 将实例对象存入数据库
        u.instance.save()
    return redirect("/user/login")


def info(request):
    return render(request, "user_center_info.html")


def site(request):
    a_info = AddressInfo.objects.all()

    return render(request, "user_center_site.html", {"data": a_info})


def get_site(request):
    data = request.POST.dict()
    user_id = request.session["user"]["id"]
    user = User.objects.get(id=user_id)
    AddressInfo.objects.create(name=data["name"], tel=data["tel"], address=data["adress"], postcode=data["postcode"],
                               user=user)
    return redirect(to="/user/user_center_site")


def order(request):
    return render(request, "user_center_order.html")
