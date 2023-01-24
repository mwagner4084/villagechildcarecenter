from django.views.generic import TemplateView
from django.shortcuts import render
from .models import HTMLModel

class HomePageView(TemplateView):
    template_name = "index.html"
    

class WelcomePageView(TemplateView):
    template_name = "welcome.html"

class ClassroomPageView(TemplateView):
    template_name = "classrooms.html"

class SteamPageView(TemplateView):
    template_name = "steam.html"

class PreschoolPageView(TemplateView):
    template_name = "preschool.html"

class SchoolAgePageView(TemplateView):
    template_name = "school_age.html"

class PottyTrainingPageView(TemplateView):
    template_name = "potty_training.html"

class ContactPageView(TemplateView):
    template_name = "contact.html"

class SubscribePageView(TemplateView):
    template_name = "subscribe.html"