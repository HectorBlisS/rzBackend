from django.contrib import admin
from .models import Project, Reward

class AdminProject(admin.ModelAdmin):
	list_display = ['name','id','author','goal', 'reached', 'finish']
	list_filter = ['goal', 'reached', 'finish']

admin.site.register(Project, AdminProject)
admin.site.register(Reward)