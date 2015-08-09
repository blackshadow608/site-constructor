"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from article.views import *
from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(r'^$', 'article.views.get_main_page'),
    url(r'^rating/', 'article.views.create_delete_rating'),
    url(r'^theme/', 'article.views.change_theme'),
    url(r'^menu/', 'article.views.change_menu'),
    url(r'^get_all_pages/', 'article.views.get_all_pages'),
    url(r'^change_site_name/', 'article.views.change_site_name'),
    url(r'^remove_page/', 'article.views.remove_page'),
    url(r'^like/', 'article.views.set_likes'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/$', LoginFormView.as_view()),
    url(r'^logout/$', 'article.views.logout'),
    url(r'^register/$', RegisterFormView.as_view()),
    url(r'^editor/(?P<ids>\w{0,50})/', "article.views.edit_view"),
    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^my_projects/', 'article.views.get_user_projects'),
    url(r'^search-form/', 'article.views.search_form'),
    url(r'^search/$', 'article.views.search'),
    #url(r'^user/(?P<id_user>\w{0,50})/', 'article.views.view_another_user'),
    url(r'^i18n/', include('django.conf.urls.i18n')),
    url(r'^view_mode/(?P<id_project>\w{0,50})/', 'article.views.view_site'),
]
