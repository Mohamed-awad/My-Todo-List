from django.urls import reverse_lazy
from .forms import UserCreateForm
from django.views.generic import CreateView
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from .serializer import UserSerializer, GroupSerializer

class SignUp(CreateView):
    form_class = UserCreateForm
    success_url = reverse_lazy('listAll')
    template_name = 'accounts/signup.html'


class UserViewSet(viewsets.ModelViewSet):
  queryset = User.objects.all().order_by('-date_joined')
  serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
  queryset = Group.objects.all()
  serializer_class = GroupSerializer



