from django.contrib import admin
from . import models

@admin.register(models.List)
class ListAdmin(admin.ModelAdmin):
    pass

@admin.register(models.Developer)
class DeveloperAdmin(admin.ModelAdmin):
    list_display = ['Name','Family','Email']
