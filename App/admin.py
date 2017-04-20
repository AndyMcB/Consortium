from django.contrib import admin

# Register your models here.

from App.models import UserProfile, ProjectProfile, Match, AddTask
admin.site.register(UserProfile)
admin.site.register(ProjectProfile)
admin.site.register(Match)
admin.site.register(AddTask)