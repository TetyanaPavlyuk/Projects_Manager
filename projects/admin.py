from django.contrib import admin
from projects.models import User, Project, Feedback


admin.site.register(User)
admin.site.register(Project)
admin.site.register(Feedback)
