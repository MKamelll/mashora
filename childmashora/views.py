from django.shortcuts import render
from django.http import HttpRequest, HttpResponse


def index(request: HttpRequest) -> HttpResponse:
    return render(request=request, template_name="childmashora/childmashora.djhtml")


# Create your views here.
def mother_info(request: HttpRequest) -> HttpResponse:
    return render(request=request, template_name="childmashora/motherinfo.djhtml")


def dad_info(request: HttpRequest) -> HttpResponse:
    return render(request=request, template_name="childmashora/dadinfo.djhtml")


def child_info(request: HttpRequest) -> HttpResponse:
    return render(request=request, template_name="childmashora/childinfo.djhtml")


def visit_info(request: HttpRequest) -> HttpResponse:
    return render(request=request, template_name="childmashora/visitinfo.djhtml")


def visit_topics(request: HttpRequest) -> HttpResponse:
    return render(request=request, template_name="childmashora/visittopics.djhtml")
