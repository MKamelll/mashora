from django.shortcuts import render
from django.http import HttpRequest, HttpResponse


# Create your views here.
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
