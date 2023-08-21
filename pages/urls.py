from django.urls import path

from api.views import send_email, submit_contact, submit_information_request

from .views import (ClassroomPageView, ConfirmPageView, ContactPageView,
                    EmploymentPageView, HomePageView, PreschoolPageView,
                    SchoolAgePageView, SteamPageView, WelcomePageView)

urlpatterns = [
    path("confirm/", ConfirmPageView.as_view(), name="confirm"),
    path("welcome/", WelcomePageView.as_view(), name="welcome"),
    path("classrooms/", ClassroomPageView.as_view(), name="classrooms"),
    path("steam/", SteamPageView.as_view(), name="steam"),
    path("preschool/", PreschoolPageView.as_view(), name="preschool"),
    path("school-age/", SchoolAgePageView.as_view(), name="school_age"),
    path("contact/", ContactPageView.as_view(), name="contact"),
    path("employment/", EmploymentPageView.as_view(), name="employment"),
    path("submit-contact/", submit_contact, name="submit_contact"),
    path("submit-information-request/", submit_information_request,
         name="submit_information_request"),
    path("send-email/", send_email, name="send_email"),
    path("", HomePageView.as_view(), name="home"),
]
