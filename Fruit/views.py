from django.shortcuts import render, redirect
from commodity.models import Commodity

def index(request):
    commodity = Commodity.objects.all()
    print(commodity)
    return render(request, "index.html", {"data":commodity})

