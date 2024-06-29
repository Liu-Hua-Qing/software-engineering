from django.db import models
from django.utils import timezone

# Create your models here.
class FishNumber(models.Model):
    total = models.IntegerField()
    add = models.IntegerField()
    minus = models.IntegerField()
    score = models.IntegerField(default=0)  # 新增的 score 字段
    
    def __str__(self):
        return f"Total: {self.total}, Add: {self.add}, Minus: {self.minus}"
    
class FishData(models.Model):
    kind = models.CharField(max_length=100)
    weight = models.FloatField()
    length = models.FloatField()
    height = models.FloatField()
    width = models.FloatField()

    def __str__(self):
        return f"Kind: {self.kind}, Weight: {self.weight}, Length: {self.length}, Height: {self.height}, Width: {self.width}"
    
class Information(models.Model):
    v = models.FloatField(verbose_name='V')
    salt = models.FloatField(verbose_name='Salt')
    oxygen = models.FloatField(verbose_name='Oxygen')
    ntu = models.FloatField(verbose_name='NTU')
    ph = models.FloatField(verbose_name='PH')
    tem = models.FloatField(verbose_name='Temperature')

    def __str__(self):
        return f"Information(v={self.v}, salt={self.salt}, oxygen={self.oxygen}, ntu={self.ntu}, ph={self.ph}, tem={self.tem}, date={self.date})"