from django.db import models
from django.conf import settings
from django.urls import reverse
from django.utils.translation import gettext_lazy as _ # https://docs.djangoproject.com/en/4.2/ref/models/fields/#enumeration-types
from django.utils import timezone

import warnings

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
	
	def sort(self):
		if self.sort_criterion == SortCriterion.BY_PRIORITY:
			return self.task_set.order_by("priority")
		elif self.sort_criterion == SortCriterion.BY_END_DATE:
			return self.task_set.order_by("end_date")
		else:
			warnings.warn("Invalid sort criterion encountered.", UserWarning)
			return self.task_set.all()

class Task(models.Model):
	list = models.ForeignKey(List, on_delete=models.CASCADE)

	title = models.CharField(max_length=255)
	#date = models.DateTimeField(auto_now_add=True)

	end_date = models.DateField() #Or DateField
	priority = models.IntegerField()
	is_done = models.BooleanField(default=False)

	def __str__(self):
		return self.title
	
	def toggle_done(self):
		self.is_done = not self.is_done
		self.save()

	def should_show_alarm(self):
		#Returns true when `end_date` is tomorrow or today
		now = timezone.now().date()
		tomorrow = now + timezone.timedelta(days=1)
		return self.end_date == now or self.end_date == tomorrow