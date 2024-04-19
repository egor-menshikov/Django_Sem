from django.db import models
from django.utils import timezone


# Create your models here.
class CoinToss(models.Model):
    result = models.CharField(max_length=5)
    date_thrown = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'id: {self.pk}, result: {self.result}, time: {self.date_thrown}\n'

    @staticmethod
    def statistics():
        stats = CoinToss.objects.order_by('-date_thrown')[:5]
        stats_dict = {}
        for item in stats:
            stats_dict[item.pk] = item.result
        return stats_dict
