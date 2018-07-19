from django.shortcuts import render, redirect
from .models import Task
from django.views.generic import (CreateView)
from django.contrib.auth.mixins import LoginRequiredMixin


class todoListCreateView(LoginRequiredMixin, CreateView):

    fields = ['name']

    def get(self, request, *args, **kwargs):
        tasks = Task.objects.filter(user=self.request.user)
        return render(self.request, 'task/index.html', {'tasks': tasks})

    def post(self, request, *args, **kwargs):

        if self.request.method == "POST":
            if 'name' in self.request.POST and self.request.POST['name'] != '':
                name = self.request.POST['name']
                user = self.request.user
                task = Task(name=name, user=user)
                task.save()

            elif 'task_delete' in self.request.POST:
                deleted = self.request.POST["task_delete"]
                task = Task.objects.get(id=int(deleted))
                task.delete()
        return redirect('/todolist/')
