from django.views.generic import TemplateView
#from django.shortcuts import render
from .models import Page

class PageView(TemplateView):
    model = Page
    handle = 'home'
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super(TemplateView, self).get_context_data(**kwargs)
        pages = Page.objects.filter(handle=self.handle)
        if len(pages):
            context['page'] = pages[0]
        return context


class HomePageView(PageView):
    template_name = "index.html"
    handle = 'home'

class WelcomePageView(PageView):
    template_name = "welcome.html"
    handle = 'philosophy'

class ClassroomPageView(PageView):
    template_name = "classrooms.html"
    handle = 'classrooms'

class SteamPageView(PageView):
    template_name = "steam.html"
    handle = 'steam'

class PreschoolPageView(PageView):
    template_name = "preschool.html"
    handle = 'preschool'

class SchoolAgePageView(PageView):
    template_name = "school_age.html"
    handle = 'school_age'

class PottyTrainingPageView(PageView):
    template_name = "potty_training.html"
    handle = 'potty_training'

class ContactPageView(PageView):
    template_name = "contact.html"
    handle = 'contact'

class SubscribePageView(PageView):
    template_name = "subscribe.html"
    handle = 'subscribe'
