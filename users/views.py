from django.contrib.auth import authenticate, forms, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db import IntegrityError
from django.db.models.fields import CharField, EmailField
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.utils.http import is_safe_url
from .models import User
from .forms import regForm, userUpdateForm, profileUpdateForm


def login_view(request):
    if request.method == "POST":
        redirect_next = request.POST.get('next')
        form = forms.AuthenticationForm(request=request, data=request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'Loged in as {user}')
                if redirect_next:
                    return redirect(f"{redirect_next[1:]}")
                return redirect('index')
    else:
        form = forms.AuthenticationForm()

    return render(request, "users/login.html", {
        "form": form
    })


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("login"))


def register(request):
    if request.method == "POST":
        form = regForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(request, username=username, password=password)
            login(request, user)
            messages.success(
                request, f'Created account succesfully as {username}')
            return redirect('index')

    else:
        form = regForm()

    # print(form)
    return render(request, "users/register.html", {
        'form': form
    })


@login_required
def profile(request):
    if request.method == 'POST':
        uForm = userUpdateForm(request.POST, instance=request.user)
        pForm = profileUpdateForm(
            request.POST, request.FILES, instance=request.user.profile)

        if uForm.is_valid() and pForm.is_valid():
            uForm.save()
            pForm.save()
            messages.success(request, f'Profile Updated!')
            return redirect('profile')
    else:
        uForm = userUpdateForm(instance=request.user)
        pForm = profileUpdateForm(instance=request.user.profile)

    return render(request, "users/profile.html", {
        "uForm": uForm,
        "pForm": pForm
    })