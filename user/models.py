from django.db import models


# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=50, unique=True, help_text="用户名")
    password = models.CharField(max_length=100, help_text="密码")
    email = models.EmailField()
    reg_time = models.DateTimeField(auto_now=True )
    class Meta:
        db_table = "user"


class AddressInfo(models.Model):
    name = models.CharField(max_length=10, help_text="收件人")
    tel = models.CharField(max_length=20, help_text="电话")
    postcode = models.CharField(max_length=20, help_text="邮编", null=True, blank=True)
    address = models.CharField(max_length=100, help_text="收货地址")
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name="info")

    class Meta:
        db_table = "adressInfo"
