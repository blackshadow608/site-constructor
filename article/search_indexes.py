# from django.contrib.auth.models import User
# import watson
# from article.models import Project, PageProject
#
# watson.register(Project, fields="project_name")
# watson.register(User, fields='username')
# watson.register(PageProject, fields=('page_name', 'text'))

# from haystack import indexes
# from article.models import Project,PageProject
#
# class ProjectIndex(indexes.SearchIndex, indexes.Indexable):
#     text = indexes.CharField(document=True, use_template=True)
#     project_name = indexes.CharField(model_attr='project_name')
#
#     def get_model(self):
#         return Project
#
#     def index_queryset(self, using=None):
#         """Used when the entire index for model is updated."""
#         return self.get_model().objects.filter(project_name="abcd")
