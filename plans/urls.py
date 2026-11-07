from django.http import HttpResponse
from django.urls import path


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
    path("", task_list, name="task_list"),
    path("task/create/", task_create, name="task_create"),
    path("task/<int:pk>/", task_detail, name="task_detail"),
    path("task/<int:pk>/edit/", task_update, name="task_update"),
    path("task/<int:pk>/delete/", task_delete, name="task_delete"),
]
