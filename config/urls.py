"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url
from django.urls import path
from todoList.task import views
from django.conf.urls import include

from rest_framework import routers
from todoList.accounts.views import UserViewSet, GroupViewSet
from todoList.task.views import TaskViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'mytasks', TaskViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('todolist/', views.todoListCreateView.as_view(), name='listAll'),
    path('accounts/', include('todoList.accounts.urls', namespace='accounts')),
    url(r'^', include(router.urls)),
    url(r'^api-auth', include('rest_framework.urls', namespace='rest_framework')),
]
