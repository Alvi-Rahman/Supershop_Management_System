from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from .forms import UserRegistrationForm, UserLoginForm, CategoryForm
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
    return render(request, 'home_page.html',
                  {
                      'logout': request.user.is_authenticated,
                      'home': 'active'
                  })


@login_required(login_url='/login/')
def admin_home(request):
    return render(request, 'admin_home.html',
                  {
                      'logout': request.user.is_authenticated,
                      "admin": 1,
                      "admin_home": "active"
                  })


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
    elif request.method == 'GET':
        if request.user.is_authenticated:
            return redirect('home')
        else:
            form = UserRegistrationForm()
            return render(request, 'all_forms.html', {'form': form,
                                                      "btn_name": "SignUp",
                                                      "title": "Sign Up",
                                                      "active": "active"})


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
    elif request.method == 'GET':
        if request.user.is_authenticated:
            return redirect('home')
        else:
            form = UserLoginForm()
            return render(request, "all_forms.html", context={"form": form,
                                                              "btn_name": "Login",
                                                              "title": "Login",
                                                              "active": "active"})


def logout_view(request):
    logout(request)
    return redirect('login')


def admin_logout_view(request):
    logout(request)
    return redirect('supershop_admin')


def supershop_admin(request):
    if request.method == "POST":
        form = UserLoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_superuser:
                    login(request, user)
                    return redirect("admin_home")
                else:
                    messages.error(request, "You are not a superuser")
                    return redirect("supershop_admin")
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    elif request.method == 'GET':
        if request.user.is_authenticated:
            return redirect('home')
        else:
            form = UserLoginForm()
            return render(request, "all_forms.html", context={"form": form,
                                                              "btn_name": "Login",
                                                              "title": "Admin Login",
                                                              "admin_login": "active"})


def admin_category(request):
    if request.method == 'GET':
        return render(request, "category.html",
                      context={"title": "Category",
                               "admin": 1,
                               "admin_category": "active"
                               })


def admin_product(request):
    if request.method == 'GET':
        return render(request, "product.html",
                      context={"title": "Product",
                               "admin": 1,
                               "admin_product": "active"
                               })

def admin_category_operation(request, ops):
    if request.method == "POST":
        if ops == 'add':
            form = CategoryForm(request.POST)
            if form.is_valid():
                messages.success(request, "Succesfully added.")
                form.save()
            else:
                messages.error(request, "Something Went Wrong.")
            return redirect("/supershop_admin/category/add/")
    elif request.method == 'GET':
        if ops == 'add':
            form = CategoryForm()
            return render(request, "all_forms.html",
                          context={"form": form,
                                   "title": "Add Category",
                                   "admin": 1,
                                   'logout': request.user.is_authenticated,
                                   "btn_name": "ADD Category",
                                   "admin_category": "active"})


def admin_product_operation(request, ops):
    pass
