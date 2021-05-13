from django.contrib import messages
from django.shortcuts import render
# from django.views import View
# from django.views.generic import (TemplateView, ListView)
# from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login, authenticate, logout
from .forms import UserRegistrationForm, UserLoginForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
import json


# class HomePage(LoginRequiredMixin, View):
#     template_name = "supershop_app/index.html"
#
#     def get(self, request):
#         # paraphrase_class = ParaphraseTool()
#         return render(request, self.template_name, context={'get': 1})
#
#     def post(self, request):
#         return render(request, self.template_name)

@login_required(login_url='/login/')
def home(request):
    return render(request, 'home_page.html')


def signup(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserRegistrationForm()
    return render(request, 'signup.html', {'form': form})


def login_view(request):
    if request.method == "POST":
        form = UserLoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("home")
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = UserLoginForm()
    return render(request, "login.html", context={"login_form": form})


def logout_view(request):
    logout(request)
    return redirect('login')
