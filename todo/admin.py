from django.contrib import admin
from .models import Task, FamilyMember, WorkDone, Parents

# Register your models here.
admin.site.register(Task)
admin.site.register(FamilyMember)
admin.site.register(WorkDone)
admin.site.register(Parents)
