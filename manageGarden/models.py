from django.db import models
from userAuth.models import User

class plant(models.Model):
    users = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(blank=False)
    water_consumption = models.IntegerField(blank=False)


