from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class PostModel(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, blank=False, null=False)
    bio = models.TextField(blank=False, null=False)
    logo = models.ImageField(blank=False, null=False, upload_to='images/posty')
    price = models.DecimalField(blank=False, null=False, max_digits=9, decimal_places=2)

    def __str__(self):
        return self.name
