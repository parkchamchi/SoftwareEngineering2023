from django import forms
from django.forms import DateInput

from .models import Task

from datetime import datetime, timedelta

class TaskForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields["title"].initial = "New task"
		self.fields["end_date"].initial = datetime.now().date() + timedelta(days=1) #tomorrow
		self.fields['priority'].initial = 10

	class Meta:
		model = Task
		fields = ("title", "end_date", "priority")
		widgets = {
			"end_date": DateInput(attrs={"type": "date"}), #Renders a date input
		}