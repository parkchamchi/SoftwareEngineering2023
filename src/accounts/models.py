from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
	#An example: (age: int,)
	#age = models.PositiveIntegerField(null=True, blank=True)
	pass