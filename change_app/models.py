from django.db import models



AMOUNT_CHOICE = (
    '5000', '',
    '2000', '',
    '1000', '',
    '500', '',
    '200', '',
    '100', '',
)


class Amount(models.Model):
    total_amount = models.IntegerField()
    change = models.IntegerField(choices=AMOUNT_CHOICE)
    multiplier = models.IntegerField()

    def __str__(self):
        return self.total_amount
    