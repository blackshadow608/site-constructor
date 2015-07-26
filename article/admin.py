from django.contrib import admin
from article.models import Comments, Article, Project, PageProject

# Register your models here.
class ArticleInline(admin.StackedInline):
    model = Comments
    extra = 2

class ArticleAdmin(admin.ModelAdmin):
    fields = ['title','text','date']
    inlines = [ArticleInline]
    list_filter = ['date','title','likes']

class ProjectInline(admin.StackedInline):
    model = PageProject
    extra = 1

class ProjectAdmin(admin.ModelAdmin):
    fields = ['project_user','project_name']
    inlines = [ProjectInline]

admin.site.register(Article, ArticleAdmin)
admin.site.register(Project, ProjectAdmin)

