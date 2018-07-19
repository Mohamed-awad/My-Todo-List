from django.urls import reverse_lazy
from .forms import UserCreateForm
from django.views.generic import CreateView


class SignUp(CreateView):
    form_class = UserCreateForm
    success_url = reverse_lazy('listAll')
    template_name = 'accounts/signup.html'

