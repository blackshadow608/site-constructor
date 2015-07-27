from django.contrib import admin
from article.models import Project, PageProject

# Register your models here.

class ProjectInline(admin.StackedInline):
    model = PageProject
    extra = 1

class ProjectAdmin(admin.ModelAdmin):
    fields = ['project_user','project_name']
    inlines = [ProjectInline]

admin.site.register(Project, ProjectAdmin)

