from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
	class Meta:
		model = CustomUser
		#Example: adds field "age", as in ./models.py
		fields = UserCreationForm.Meta.fields #+ ("age",)

class CustomUserChangeForm(UserChangeForm):
	class Meta:
		model = CustomUser
		fields = UserChangeForm.Meta.fields
