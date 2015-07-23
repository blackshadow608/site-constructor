from django.contrib import admin
from article.models import Comments, Article

# Register your models here.
class ArticleInline(admin.StackedInline):
    model = Comments
    extra = 2

class ArticleAdmin(admin.ModelAdmin):
    fields = ['title','text','date']
    inlines = [ArticleInline]
    list_filter = ['date','title','likes']

admin.site.register(Article, ArticleAdmin)
