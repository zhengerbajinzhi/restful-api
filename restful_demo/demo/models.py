from django.db import models
import django.utils.timezone as timezone


# Create your models here.


class IpPool(models.Model):
    '''IP池'''

    agreement = models.CharField(verbose_name='协议类型', max_length=10, null=True)
    ip_address = models.CharField(verbose_name='IP地址', max_length=64)
    create_time = models.DateTimeField(verbose_name='创建时间', default=timezone.now)
    update_time = models.DateTimeField(verbose_name='更新时间', auto_now=True)

    def __str__(self):
        return self.ip_address

    class Meta:
        db_table = 'ip_pool'
