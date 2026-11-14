from django.http import HttpResponse
from django.urls import path
from .views import TaskListView, TaskDetailView, AddComentView


def task_list(request):
    return HttpResponse("Task list")


def task_detail(request, pk):
    return HttpResponse(f"Task detail: {pk}")


def task_create(request):
    return HttpResponse("Create task")


def task_update(request, pk):
    return HttpResponse(f"Update task: {pk}")


def task_delete(request, pk):
    return HttpResponse(f"Delete task: {pk}")


app_name = "plans"

urlpatterns = [
    path("", TaskListView.as_view(), name="task_list"),
    path("task/create/", task_create, name="task_create"),
    path("task/<int:pk>/", TaskDetailView.as_view(), name="task_detail"),
    path("task/<int:pk>/edit/", task_update, name="task_update"),
    path("task/<int:pk>/delete/", task_delete, name="task_delete"),
    path("task/<int:pk>/comment/", AddComentView.as_view(), name="comment_create"),
]

