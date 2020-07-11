from django.shortcuts import render
from .models import Commodity, Cart
from django.http import HttpResponse
# Create your views here.
import json
from user.models import User


# 商品详情页
def detail(request, id):
    data = Commodity.objects.get(id=id)
    return render(request, "detail.html", {"data": data})


# 购物车页面
def cart(request):
    commo = Cart.objects.filter(user=request.session["user"]["id"])
    commo_list = []
    commo_dict = {}

    for item in commo:
        commodity = Commodity.objects.get(id=item.commodity_id)
        commo_dict["id"] = item.id
        commo_dict["commodity"] = commodity
        commo_dict["num"] = item.num
        commo_price = commodity.commodity_price
        # round()保留两位小数
        commo_dict["price"] = "%.2f" % (int(item.num) * float(commodity.commodity_price))
        commo_list.append(commo_dict)
        commo_dict = {}

    return render(request, "cart.html", {"data": commo_list, "data_len": len(commo_list)})


# 加入购物车
def getIn_cart(request, id):
    try:
        c = Cart.objects.get(id=id)
    except:
        num = request.POST.dict()["num"]
        user = request.session["user"]["id"]
        cart = Cart.objects.create(commodity=Commodity.objects.get(id=id), user=user, num=num)
        if cart:
            msg = {"status": 200}
        else:
            msg = {"status": 500}
        return HttpResponse(json.dumps(msg))
    else:
        num = int(c.num) + int(request.POST.dict()["num"])
        Cart.objects.filter(id=id).update(num=num)
        return HttpResponse(json.dumps({"status": 200}))


# 购物车删除
def del_comm(request, id):
    Cart.objects.filter(id=id).delete()
    return HttpResponse()


def order(request):
    return render(request, "place_order.html")