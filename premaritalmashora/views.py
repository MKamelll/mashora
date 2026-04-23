from django.shortcuts import render
from django.http import HttpRequest, HttpResponse


# Create your views here.
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
