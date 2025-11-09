from django.contrib import admin
from .models import (
    InfoModel,
    SkillModel,
    DegreeModel,
    PortfolioModel,
    ContactModel,
)


class InfoModel_admin(admin.ModelAdmin):
    list_display = ['__str__']
    ordering = ['-id']

class SkillModel_admin(admin.ModelAdmin):
    list_display = ['skill', 'percent', 'title']
    ordering = ['-id']

class DegreeModel_admin(admin.ModelAdmin):
    list_display = ['title']
    ordering = ['-id']

class PortfolioModel_admin(admin.ModelAdmin):
    list_display = ['title', 'created']
    ordering = ['-id']

class ContactModel_admin(admin.ModelAdmin):
    list_display = ['name', 'created', 'is_read']
    ordering = ['-id']


admin.site.register(InfoModel, InfoModel_admin)
admin.site.register(SkillModel, SkillModel_admin)
admin.site.register(DegreeModel, DegreeModel_admin)
admin.site.register(PortfolioModel, PortfolioModel_admin)
admin.site.register(ContactModel, ContactModel_admin)