from django.db import models



class Amount(models.Model):
    total_amount = models.IntegerField(null=True, blank=True)
    multiplier = models.IntegerField(null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        
        return str(self.total_amount)
    
