from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('tasks/', views.list_t, name="tasks"),
    path('new/', views.create_task, name="create"),
    path('delete/<int:task_id>/', views.delete, name="delete"),
    path('edit/<int:task_id>/', views.edit, name="edit"),
    path('update/<int:task_id>', views.update, name="update")
]
