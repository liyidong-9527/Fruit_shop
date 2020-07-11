from django.urls import path
from . import views

urlpatterns =[
    path("register", views.reg),
    path("login", views.login),
    path("reg_user", views.reg_user),
    path("user_center_info", views.info),
    path("user_login", views.user_login),
    path("user_center_site", views.site),
    path("user_center_order", views.order),
    path("get_site", views.get_site),
]