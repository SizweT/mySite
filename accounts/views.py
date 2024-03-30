# accounts/views.py
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.http import HttpResponse
from django.views.generic import View


class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"


class UserProfileView(View):
    def get(self, request):
        # Logic to retrieve user profile information
        return HttpResponse("Welcome to your profile Page")
