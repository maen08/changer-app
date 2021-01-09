from django.db import models



class Amount(models.Model):
    total_amount = models.IntegerField()
    change = models.IntegerField()
    multiplier = models.IntegerField()

    def __str__(self):
        return self.total_amount
    