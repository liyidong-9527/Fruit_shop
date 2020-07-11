from django.urls import path
from . import views

urlpatterns = [
    path("detail/<int:id>", views.detail),
    path("cart", views.cart),
    path("cart/<int:id>", views.getIn_cart),
    path("del_comm/<int:id>", views.del_comm),
    path("place_order", views.order)
]