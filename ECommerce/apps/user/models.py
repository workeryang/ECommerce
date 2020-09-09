from django.db import models


class Order(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=24, verbose_name='订单名', null=True, blank=True)
    price = models.DecimalField(verbose_name='金额', max_digits=8, decimal_places=2, blank=True, null=True)
    add_time = models.DateTimeField(verbose_name='创建日期', auto_now_add=True)
    
    def __str__(self):
        return self.title
