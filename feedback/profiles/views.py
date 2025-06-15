import re
from django.shortcuts import render
from django.views import View
from django.http import HttpResponseRedirect
from .forms import ProfileForm
from .models import UserProfile

# Create your views here.




class CreateProfileView(View):
    def get(self, request):
        form = ProfileForm()
        return render(request, "profiles/create_profile.html", {"form": form})

    def post(self, request):
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile_picture = form.cleaned_data["profile_picture"]
            if profile_picture:
                profile = UserProfile(profile_picture=profile_picture)
                profile.save()
                return HttpResponseRedirect("/profiles")
            
        return render(request, "profiles/create_profile.html", {"form": form})