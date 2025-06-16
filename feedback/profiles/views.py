import re
from django.shortcuts import render
from django.views import View
from django.http import HttpResponseRedirect
from .forms import ProfileForm
from .models import UserProfile
from django.views.generic.edit import CreateView
from django.views.generic import ListView
# Create your views here.

class CreateProfileView(CreateView):
    model = UserProfile
    fields = '__all__'
    template_name = "profiles/create_profile.html"
    success_url = "/profiles"


class ProfileView(ListView):
    model = UserProfile
    template_name = "profiles/user_profile.html"
    context_object_name = "profiles"