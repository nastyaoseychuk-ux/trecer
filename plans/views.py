
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import To_do, Comment

class TaskListView(ListView):
    model = To_do
    template_name = 'task_list.html'
    context_object_name = 'tasks'
    ordering = ['-created_at']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['statuses'] = [
            ('pending', 'До виконання'),
            ('in_progress', 'У процесі'),
            ('completed', 'Виконано'),
        ]

        context['pending_count'] = self.object_list.filter(status='pending').count()
        context['in_progress_count'] = self.object_list.filter(status='in_progress').count()
        context['completed_count'] = self.object_list.filter(status='completed').count()

        return context


class TaskDetailView(DetailView):
    model = To_do
    template_name = 'task_detail.html'
    context_object_name = 'task'


class AddComentView(LoginRequiredMixin, CreateView):
    model = Comment
    template_name = 'task_detail.html'
    fields = ['content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.task = get_object_or_404(
            To_do,
            pk=self.kwargs['pk']
        )
        return super().form_valid(form)

    def get_success_url(self):
        return reverse(
            'plans:task_detail',
            kwargs={'pk': self.kwargs['pk']}
        )