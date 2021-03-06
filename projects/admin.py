from django.contrib import admin
from .models import Project, Reward, Category, Observaciones, Follow, Updates

class AdminProject(admin.ModelAdmin):
	list_display = ['name','id','author','goal', 'reached', 'finish']
	list_filter = ['goal', 'reached', 'finish']


class AdminCategory(admin.ModelAdmin):
	list_display = ['name','id', 'slug']
	prepopulated_fields = {'slug':('name',)}

admin.site.register(Project, AdminProject)
admin.site.register(Reward)
admin.site.register(Category, AdminCategory)
admin.site.register(Observaciones)
admin.site.register(Follow)
admin.site.register(Updates)