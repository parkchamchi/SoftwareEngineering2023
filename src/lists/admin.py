from django.contrib import admin

from .models import List, Task

# Register your models here.

class TaskInline(admin.TabularInline):
	model = Task
	extra = 0
	
class ListAdmin(admin.ModelAdmin):
	inlines = [
		TaskInline,
	]

admin.site.register(List, ListAdmin)
admin.site.register(Task)