from . import views
from django.urls import path,re_path


app_name = 'articles'

urlpatterns = [
    path('create/', views.article_create, name="create"),
    re_path(r'^(?P<slug>[\w-]+)/$', views.article_detail, name="detail"),
    path('', views.article_list, name="list"),
]
