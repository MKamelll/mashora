from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse, HttpResponseServerError
from .forms import RegisterForm


def index(request: HttpRequest) -> HttpResponse:
    return render(request=request, template_name="ui/index.djhtml")


def register(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
        else:
            return render(
                request=request,
                template_name="ui/register.djhtml",
                context={"form": form},
            )
    else:
        form = RegisterForm()
    return render(
        request=request, template_name="ui/register.djhtml", context={"form": form}
    )


def login(request: HttpRequest) -> HttpResponse:
    return render(request=request, template_name="ui/login.djhtml")


def general(request: HttpRequest) -> HttpResponse:
    return render(request=request, template_name="ui/general.djhtml")


def submit_general(request: HttpRequest) -> HttpResponse | HttpResponseServerError:
    if request.method == "POST":
        match request.POST.get("mashora_kind"):
            case "for-child":
                return render(
                    request=request, template_name="ui/childmashora/childmashora.djhtml"
                )
            case "for-pre-marital":
                is_first_meeting = True
                if request.POST.get("pre_marital_first_meeting") == "false":
                    is_first_meeting = False
                return render(
                    request=request,
                    template_name="ui/premaritalmashora/premaritalmashora.djhtml",
                    context={"is_first_meeting": is_first_meeting},
                )
            case _:
                return index(request=request)

    return HttpResponseServerError("Something went wrong trying to submit_general")


# child mashora
def mother_info(request: HttpRequest) -> HttpResponse:
    return render(request=request, template_name="ui/childmashora/motherinfo.djhtml")


def dad_info(request: HttpRequest) -> HttpResponse:
    return render(request=request, template_name="ui/childmashora/dadinfo.djhtml")


def child_info(request: HttpRequest) -> HttpResponse:
    return render(request=request, template_name="ui/childmashora/childinfo.djhtml")


def visit_info(request: HttpRequest) -> HttpResponse:
    return render(request=request, template_name="ui/childmashora/visitinfo.djhtml")


def visit_topics(request: HttpRequest) -> HttpResponse:
    return render(request=request, template_name="ui/childmashora/visittopics.djhtml")


# pre marital mashora
def female_info(request: HttpRequest) -> HttpResponse:
    return render(
        request=request, template_name="ui/premaritalmashora/femaleinfo.djhtml"
    )


def male_info(request: HttpRequest) -> HttpResponse:
    return render(request=request, template_name="ui/premaritalmashora/maleinfo.djhtml")


def meeting_info(request: HttpRequest) -> HttpResponse:
    return render(
        request=request, template_name="ui/premaritalmashora/meetinginfo.djhtml"
    )


def meeting_topics(request: HttpRequest) -> HttpResponse:
    return render(
        request=request, template_name="ui/premaritalmashora/meetingtopics.djhtml"
    )
