from django.contrib.auth.admin import UserAdmin
import watson
from article.models import Project, PageProject, Gallery
from django.contrib import admin
from django.contrib.auth.models import User

# Register your models here.
admin.site.disable_action('delete_selected')

class ProjectInline(admin.StackedInline):
    model = PageProject
    extra = 0


class ProjectAdmin(admin.ModelAdmin):
    actions = [admin.site.get_action('delete_selected')]
    fields = ['project_user', 'project_name', 'project_is_dark', 'project_menu_is_horizontal']
    inlines = [ProjectInline]


class GalleryAdmin(admin.ModelAdmin):
    actions = [admin.site.get_action('delete_selected')]

    fields = ['user', 'image']


class UserProfileAdmin(UserAdmin):
    def delete_model(self, request, obj):
        if type(obj) == User and obj == request.user:
            print('asdasdas')
            return False
        else:
            obj.delete()

admin.site.register(Project, ProjectAdmin)
admin.site.register(Gallery, GalleryAdmin)
admin.site.unregister(User)
admin.site.register(User, UserProfileAdmin)

# watson.register(Project,fields=("project_name",))
# watson.register(PageProject, fields=("page_name","text",))
# watson.register(User, fields=("username",))