from django.db import models

class Expense(models.Model):
    item = models.CharField(max_length=100)
    cost = models.FloatField()
    currency = models.CharField(max_length=10)
    purchased_date = models.DateField()
    completion_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.item
