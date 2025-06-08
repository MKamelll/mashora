from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, HttpResponseServerError

def index(request: HttpRequest) -> HttpResponse:
    return render(request=request, template_name="main/index.html")

def general(request: HttpRequest) -> HttpResponse:
    return render(request=request, template_name="main/general.html")

def submit_general(request: HttpRequest) -> HttpResponse | HttpResponseServerError:
    if request.method == "POST":
        match request.POST.get("mashora_kind"):
            case "for-child":
                return render(request=request, template_name="main/childmashora/childmashora.html")
            case "for-pre-marital":
                is_first_meeting = True
                if request.POST.get("pre_marital_first_meeting") == "false":
                    is_first_meeting = False 
                return render(request=request, template_name="main/premaritalmashora/premaritalmashora.html",
                       context={ "is_first_meeting": is_first_meeting })
            case _:
                return index(request=request)
    
    return HttpResponseServerError("Something went wrong trying to submit_general")

# child mashora
def mother_info(request: HttpRequest) -> HttpResponse:
    return render(request=request, template_name="main/childmashora/motherinfo.html")

def dad_info(request: HttpRequest) -> HttpResponse:
    return render(request=request, template_name="main/childmashora/dadinfo.html")

def child_info(request: HttpRequest) -> HttpResponse:
    return render(request=request, template_name="main/childmashora/childinfo.html")

def visit_info(request: HttpRequest) -> HttpResponse:
    return render(request=request, template_name="main/childmashora/visitinfo.html")

def visit_topics(request: HttpRequest) -> HttpResponse:
    return render(request=request, template_name="main/childmashora/visittopics.html")

# pre marital mashora
def female_info(request: HttpRequest) -> HttpResponse:
    return render(request=request, template_name="main/premaritalmashora/femaleinfo.html")

def male_info(request: HttpRequest) -> HttpResponse:
    return render(request=request, template_name="main/premaritalmashora/maleinfo.html")

def meeting_info(request: HttpRequest) -> HttpResponse:
    return render(request=request, template_name="main/premaritalmashora/meetinginfo.html")

def meeting_topics(request: HttpRequest) -> HttpResponse:
    return render(request=request, template_name="main/premaritalmashora/meetingtopics.html")
