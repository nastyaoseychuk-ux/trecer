from django.db import models

class To_do(models.Model):
    STATUS_CHOICES = [
        ('pending', 'До виконання'),
        ('in_progress', 'У процесі'),
        ('completed', 'Виконано'),
    ]

    PRIORITY_CHOICES = [
        ('low', 'Низький'),
        ('medium', 'Середній'),
        ('high', 'Високий'),
    ]
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES,     default='medium')
    
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE,  related_name = 'tasks')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    completed_at = models.DateTimeField(null=True, blank=True)
    
    attachments = models.FileField(upload_to='attachments/', null=True, blank=True)

    executors = models.ManyToManyField('auth.User', related_name='assigned_tasks', blank=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    task = models.ForeignKey(To_do, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    attachments = models.FileField(upload_to='comment_attachments/', null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment on {self.task.title} at {self.created_at}"