from django.urls import path
from . import views

urlpatterns = [
    path("visittopics/", view=views.visit_topics, name="visittopics"),
    path("visitinfo/", view=views.visit_info, name="visitinfo"),
    path("childinfo/", view=views.child_info, name="childinfo"),
    path("dadinfo/", view=views.dad_info, name="dadinfo"),
    path("motherinfo/", view=views.mother_info, name="motherinfo"),
]
