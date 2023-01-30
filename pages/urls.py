from django.urls import path
from .views import (
    HomePageView,
    WelcomePageView,
    ClassroomPageView,
    SchoolAgePageView,
    SteamPageView,
    PreschoolPageView,
    ContactPageView,
    SubscribePageView,
)

urlpatterns = [
    path("subscribe/", SubscribePageView.as_view(), name="subscribe"),
    path("welcome/", WelcomePageView.as_view(), name="welcome"),
    path("classrooms/", ClassroomPageView.as_view(), name="classrooms"),
    path("steam/", SteamPageView.as_view(), name="steam"),
    path("preschool/", PreschoolPageView.as_view(), name="preschool"),
    path("school-age/", SchoolAgePageView.as_view(), name="school_age"),
    path("contact/", ContactPageView.as_view(), name="contact"),
    path("", HomePageView.as_view(), name="home"),
]
