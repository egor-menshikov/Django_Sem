from django.db import models
from django.utils import timezone


# Create your models here.
class CoinToss(models.Model):
    result = models.CharField(max_length=5)
    date_thrown = models.DateTimeField(default=timezone.now)