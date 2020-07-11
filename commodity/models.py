from django.db import models
from user.models import User


# Create your models here.

class Commodity(models.Model):
    commodity_name = models.CharField(max_length=20, verbose_name="名字")
    commodity_price = models.CharField(max_length=20)
    commodity_unit = models.CharField(max_length=50)
    intorduction = models.CharField(max_length=100, help_text="简介")
    description = models.CharField(max_length=200, help_text="详情描述")
    commodity_type = models.CharField(max_length=20, help_text="商品类型", null=True, blank=True)
    img_name = models.CharField(max_length=20, null=True, blank=True, help_text="照片名")

    class Meta:
        db_table = "commodity"


class Cart(models.Model):
    user = models.IntegerField()
    num = models.IntegerField(verbose_name="数量")
    commodity = models.ForeignKey(to=Commodity, on_delete=models.CASCADE, related_name="cart")

    class Meta:
        db_table = "cart"
