from django import forms
from django.forms import DateInput

from .models import Task

class TaskForm(forms.ModelForm):
	class Meta:
		model = Task
		fields = ("title", "end_date", "priority")
		widgets = {
			"end_date": DateInput(attrs={"type": "date"}), #Renders a date input
		}