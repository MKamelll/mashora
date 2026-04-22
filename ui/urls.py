from django.urls import path
from . import views

urlpatterns = [
    # pre marital mashora
    path("femaleinfo", view=views.female_info, name="femaleinfo"),
    path("maleinfo", view=views.male_info, name="maleinfo"),
    path("meetinginfo", view=views.meeting_info, name="meetinginfo"),
    path("meetingtopics", view=views.meeting_topics, name="meetingtopics"),
    # child mashora
    path("visittopics/", view=views.visit_topics, name="visittopics"),
    path("visitinfo/", view=views.visit_info, name="visitinfo"),
    path("childinfo/", view=views.child_info, name="childinfo"),
    path("dadinfo/", view=views.dad_info, name="dadinfo"),
    path("motherinfo/", view=views.mother_info, name="motherinfo"),
    # general
    path("submitgeneral/", view=views.submit_general, name="submitgeneral"),
    path("general/", view=views.general, name="general"),
    # registeration
    path("register/", view=views.register, name="register"),
    path("login/", view=views.login, name="login"),
    path("", view=views.index, name="index"),
]
