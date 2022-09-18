from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=50, null=False)
    description = models.CharField(default="", max_length=500)
    price = models.FloatField(default=0.0)

    def __str__(self):
        return f"'{self.name}' {self.price:.2f}RUB"
