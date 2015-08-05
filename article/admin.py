from django.contrib import admin
from article.models import Project, PageProject, Gallery

# Register your models here.

class ProjectInline(admin.StackedInline):
    model = PageProject
    extra = 0

class ProjectAdmin(admin.ModelAdmin):
    fields = ['project_user','project_name','project_is_dark','project_menu_is_horizontal']
    inlines = [ProjectInline]

class GalleryAdmin(admin.ModelAdmin):
    fields = ['user','image']
admin.site.register(Project, ProjectAdmin)
admin.site.register(Gallery,GalleryAdmin)

