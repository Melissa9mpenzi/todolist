from django.contrib import admin
from django.urls import path
from .import views


urlpatterns = [
    path('', views.home, name = 'home'),
    path('family_members/', views.familymember, name = 'family_members'),
    path('add_family_member/', views.add_family_member, name = 'add_family_member'),
    path('task/', views.task, name ='task'),
    path('add_tasks/', views.add_tasks, name = 'add_task'),
    path('work_done/', views.work_done, name = 'work_done'),
    path('addwork_done/', views.add_work_done, name = 'addwork_done'),
]