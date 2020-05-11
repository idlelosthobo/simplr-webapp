from app.registration.forms import RegisterForm, UserEditForm
from app.registration.models import UserProfile
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect, reverse


def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)

        if form.is_valid():
            user_form = form.save()
            user_form.is_employee = False
            user_form.save()

            user = authenticate(username=response.POST['username'], password=response.POST['password1'])

            user_profile = UserProfile(user=user)
            user_profile.save()

            return redirect(reverse('character_select_view'))

        else:

            return redirect("/accounts/register")

    else:
        form = RegisterForm()

    return render(response, "registration/register_form.html", {"form": form})


def register_success(response):

    return render(response, "registration/register_success.html", {})


