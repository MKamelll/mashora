from django.shortcuts import render
from django.http import HttpRequest, HttpResponse


# Create your views here.
def index(request: HttpRequest) -> HttpResponse:
    return render(
        request=request, template_name="premaritalmashora/premaritalmashora.djhtml"
    )


def female_info(request: HttpRequest) -> HttpResponse:
    return render(request=request, template_name="premaritalmashora/femaleinfo.djhtml")


def male_info(request: HttpRequest) -> HttpResponse:
    return render(request=request, template_name="premaritalmashora/maleinfo.djhtml")


def meeting_info(request: HttpRequest) -> HttpResponse:
    return render(request=request, template_name="premaritalmashora/meetinginfo.djhtml")


def meeting_topics(request: HttpRequest) -> HttpResponse:
    return render(
        request=request, template_name="premaritalmashora/meetingtopics.djhtml"
    )
