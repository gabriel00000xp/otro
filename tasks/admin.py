from django.contrib import admin
from .models import Task
# Register your models here.
admin.site.register(Task)
# This code registers the Task model with the Django admin site, allowing it to be managed through the admin interface.
# The Task model is defined in tasks/models.py, and it includes fields for title and description.