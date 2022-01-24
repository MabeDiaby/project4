from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name="home"),
    
    path('socials/', views.socials_list, name='socials_list'),
    path('socials/<int:pk>', views.socials_info, name='socials_info'),
    path('socials/new', views.socials_create, name='socials_create'),
    path('socials/<int:pk>/edit', views.socials_edit, name='socials_edit'),
    path('socials/<int:pk>/delete', views.socials_delete, name='socials_delete'),
    
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>', views.post_info, name='post_info'),
    path('post/new', views.post_create, name='post_create'),
    path('post/<int:pk>/edit', views.post_edit, name='post_edit'),
    path('post/<int:pk>/delete', views.post_delete, name='post_delete'),
    
    path('project/', views.project_list, name='project_list'),
    path('project/<int:pk>', views.project_info, name='project_info'),
    path('project/new', views.project_create, name='project_create'),
    path('project/<int:pk>/edit', views.project_edit, name='project_edit'),
    path('project/<int:pk>/delete', views.project_delete, name='project_delete'),
    
    path('tag/', views.tag_list, name='tag_list'),
    path('tag/<int:pk>', views.tag_info, name='tag_info'),
    path('tag/new', views.tag_create, name='tag_create'),
    path('tag/<int:pk>/edit', views.tag_edit, name='tag_edit'),
    path('tag/<int:pk>/delete', views.tag_delete, name='tag_delete'),
]