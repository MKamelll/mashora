from django.urls import path
from . import views

urlpatterns = [

    # pre marital mashora
    path('femaleinfo', view=views.female_info, name="female_info"),
    path('maleinfo', view=views.male_info, name="male_info"),
    path('meetinginfo', view=views.meeting_info, name="meeting_info"),
    path('meetingtopics', view=views.meeting_topics, name="meeting_topics"),
    
    # child mashora
    path('visittopics/', view=views.visit_topics, name='visit_topics'),
    path('visitinfo/', view=views.visit_info, name='visit_info'),
    path('childinfo/', view=views.child_info, name='child_info'),
    path('dadinfo/', view=views.dad_info, name='dad_info'),
    path('motherinfo/', view=views.mother_info, name='mother_info'),
    
    # general
    path('submitgeneral/', view=views.submit_general, name='submit_general'),
    path('general/', view=views.general, name='general'),
    path('', view=views.index, name='index'),
]
