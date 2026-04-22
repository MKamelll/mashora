from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, HttpResponseServerError
from


def index(request: HttpRequest) -> HttpResponse:
    return render(request=request, template_name="ui/index.html")


def register(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
        else:
            return render(
                request=request,
                template_name="users/register.html",
                context={"form": form},
            )
    else:
        form = RegisterForm()
    return render(
        request=request, template_name="users/register.html", context={"form": form}
    )


def login(request: HttpRequest) -> HttpResponse:
    return render(request=request, template_name="users/login.html")


def general(request: HttpRequest) -> HttpResponse:
    return render(request=request, template_name="ui/general.html")


def submit_general(request: HttpRequest) -> HttpResponse | HttpResponseServerError:
    if request.method == "POST":
        match request.POST.get("mashora_kind"):
            case "for-child":
                return render(
                    request=request, template_name="ui/childmashora/childmashora.html"
                )
            case "for-pre-marital":
                is_first_meeting = True
                if request.POST.get("pre_marital_first_meeting") == "false":
                    is_first_meeting = False
                return render(
                    request=request,
                    template_name="ui/premaritalmashora/premaritalmashora.html",
                    context={"is_first_meeting": is_first_meeting},
                )
            case _:
                return index(request=request)

    return HttpResponseServerError("Something went wrong trying to submit_general")


# child mashora
def mother_info(request: HttpRequest) -> HttpResponse:
    return render(request=request, template_name="ui/childmashora/motherinfo.html")


def dad_info(request: HttpRequest) -> HttpResponse:
    return render(request=request, template_name="ui/childmashora/dadinfo.html")


def child_info(request: HttpRequest) -> HttpResponse:
    return render(request=request, template_name="ui/childmashora/childinfo.html")


def visit_info(request: HttpRequest) -> HttpResponse:
    return render(request=request, template_name="ui/childmashora/visitinfo.html")


def visit_topics(request: HttpRequest) -> HttpResponse:
    return render(request=request, template_name="ui/childmashora/visittopics.html")


# pre marital mashora
def female_info(request: HttpRequest) -> HttpResponse:
    return render(request=request, template_name="ui/premaritalmashora/femaleinfo.html")


def male_info(request: HttpRequest) -> HttpResponse:
    return render(request=request, template_name="ui/premaritalmashora/maleinfo.html")


def meeting_info(request: HttpRequest) -> HttpResponse:
    return render(
        request=request, template_name="ui/premaritalmashora/meetinginfo.html"
    )


def meeting_topics(request: HttpRequest) -> HttpResponse:
    return render(
        request=request, template_name="ui/premaritalmashora/meetingtopics.html"
    )
