from django.db import models



class Amount(models.Model):
    total_amount = models.IntegerField(null=True, blank=True)
    change = models.IntegerField(null=True, blank=True)
    multiplier = models.IntegerField(null=True, blank=True)

    def __str__(self):
        
        return self.total_amount
    
