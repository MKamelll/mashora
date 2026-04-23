from django.urls import path

urlpatterns = [
    path("femaleinfo/", view=views.female_info, name="femaleinfo"),
    path("maleinfo/", view=views.male_info, name="maleinfo"),
    path("meetinginfo/", view=views.meeting_info, name="meetinginfo"),
    path("meetingtopics/", view=views.meeting_topics, name="meetingtopics"),
]
