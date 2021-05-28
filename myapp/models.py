from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.OneToOneField(User ,on_delete=models.CASCADE)
    address = models.CharField(max_length=100)

    def __str__(self):
        return self.user.username



