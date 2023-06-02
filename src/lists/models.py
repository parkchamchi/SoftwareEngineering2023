from django.db import models
from django.conf import settings
from django.urls import reverse
from django.utils.translation import gettext_lazy as _ # https://docs.djangoproject.com/en/4.2/ref/models/fields/#enumeration-types

# Create your models here.

class SortCriterion(models.TextChoices):
	# https://docs.djangoproject.com/en/4.2/ref/models/fields/#enumeration-types
	BY_PRIORITY = "PR"
	BY_END_DATE = "ED"

class List(models.Model):
	title = models.CharField(max_length=255)
	#date = models.DateTimeField(auto_now_add=True)
	author = models.ForeignKey(
		settings.AUTH_USER_MODEL,
		on_delete=models.CASCADE,
	)
	sort_criterion = models.CharField(
		max_length=2,
		choices=SortCriterion.choices,
		default=SortCriterion.BY_END_DATE,
	)

	def __str__(self):
		return self.title
	
	def get_absolute_url(self):
		return reverse("list_detail", kwargs={"pk": self.pk})

class Task(models.Model):
	list = models.ForeignKey(List, on_delete=models.CASCADE)

	title = models.CharField(max_length=255)
	#date = models.DateTimeField(auto_now_add=True)

	end_date = models.DateField() #Or DateField
	priority = models.IntegerField()
	is_done = models.BooleanField(default=False)

	def __str__(self):
		return self.title
