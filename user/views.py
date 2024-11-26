from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from .form import ProfileUpdateForm, UserRegisterForm, UserUpdateForm


def register(request):
    """
    Handle user registration process.

    """
    try:
        if request.method == "POST":
            form = UserRegisterForm(request.POST)
            if form.is_valid():
                form.save()
                username = form.cleaned_data.get("username")
                messages.success(
                    request,
                    f"{username} your registration is successful. You can login now",
                )
                return redirect("login")
        else:
            form = UserRegisterForm()
        return render(request, "user/register.html", {"form": form})
    except Exception as e:
        messages.error(
            request, f"An unexpected error occurred during registration: {str(e)}"
        )
        return redirect("register")


def logout_view(request):
    """
    Log out the current user.
    """
    try:
        logout(request)
        messages.success(request, "You have been logged out successfully")
        return redirect("login")
    except Exception as e:
        messages.error(request, f"Error during logout: {str(e)}")
        return redirect("blog-home")


@login_required
def profile(request):
    """
    Manage user profile updates.
    """
    try:
        if request.method == "POST":
            u_form = UserUpdateForm(request.POST, instance=request.user)
            p_form = ProfileUpdateForm(
                request.POST, request.FILES, instance=request.user.profile
            )

            if u_form.is_valid() and p_form.is_valid():
                u_form.save()
                p_form.save()
                messages.success(request, "Your profile has been updated")
                return redirect("profile")
        else:
            u_form = UserUpdateForm(instance=request.user)
            p_form = ProfileUpdateForm(instance=request.user.profile)

        context = {"u_form": u_form, "p_form": p_form}
        return render(request, "user/profile.html", context)
    except Exception as e:
        messages.error(
            request, f"An unexpected error occurred while accessing profile: {str(e)}"
        )
        return redirect("blog-home")
