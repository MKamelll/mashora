from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .forms import RegisterForm

# Create your views here.
def register(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form  = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("users/login.html")
        else:
            return render(request=request, template_name="users/register.html", context={"form": form})
    else:
        form = RegisterForm()
    return render(request=request, template_name="users/register.html", context={"form": form})