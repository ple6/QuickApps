from django.urls import reverse_lazy
from django.views import generic
from django.views.generic.edit import CreateView
from django.shortcuts import get_object_or_404


from user.models import CustomUser
from .forms import CustomUserCreationForm

from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

class UserProfileView(generic.DetailView):
    model = CustomUser
    template_name = 'listing.html'

    def get_object(self):
        return get_object_or_404(User, username=self.kwargs['username'])