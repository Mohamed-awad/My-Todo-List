from django.db import models
from django.utils import timezone

from django.contrib.auth import get_user_model
User = get_user_model()


class Task(models.Model):
    user = models.ForeignKey(User, related_name='tasks', on_delete=True)
    name = models.TextField(max_length=200)
    created_date = models.DateField(default=timezone.now())

    class Meta:
        ordering = ['-created_date']

    def __str__(self):
        return self.name
