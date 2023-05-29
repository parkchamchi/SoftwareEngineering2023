from django.db import models
from django.conf import settings
from django.urls import reverse

# Create your models here.

class List(models.Model):
	title = models.CharField(max_length=255)
	date = models.DateTimeField(auto_now_add=True)
	author = models.ForeignKey(
		settings.AUTH_USER_MODEL,
		on_delete=models.CASCADE,
	)

	def __str__(self):
		return self.title
	
	def get_absolute_url(self):
		return reverse("list_detail", kwargs={"pk": self.pk})

class Task(models.Model):
	list = models.ForeignKey(List, on_delete=models.CASCADE)

	title = models.CharField(max_length=255)
	date = models.DateTimeField(auto_now_add=True)

	end_date = models.DateTimeField() #Or DateField
	priority = models.IntegerField()

	def __str__(self):
		return self.title
