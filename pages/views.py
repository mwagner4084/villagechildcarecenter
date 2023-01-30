from django.views.generic import TemplateView
from .models import Page

class PageView(TemplateView):
    """ Base class for all page views. """

    model = Page
    handle = None
    template_name = None
    def __init__(self, *args, **kwargs):
        super(PageView, self).__init__(*args, **kwargs)
        if not self.handle or not self.template_name:
            raise Exception('You must define a handle and template_name')

    def get_context_data(self, **kwargs):
        """ Add the page to the context. """
        context = super(TemplateView, self).get_context_data(**kwargs)
        pages = Page.objects.filter(handle=self.handle)
        if len(pages):
            context['page'] = pages[0]
        return context


class HomePageView(PageView):
    """ Home page view. """

    template_name = "index.html"
    handle = 'home'

class WelcomePageView(PageView):
    """ Welcome page view. """

    template_name = "welcome.html"
    handle = 'philosophy'

class ClassroomPageView(PageView):
    """ Classroom page view. """

    template_name = "classrooms.html"
    handle = 'classrooms'

class SteamPageView(PageView):
    """ Steam page view. """

    template_name = "steam.html"
    handle = 'steam'

class PreschoolPageView(PageView):
    """ Preschool page view. """

    template_name = "preschool.html"
    handle = 'preschool'

class SchoolAgePageView(PageView):
    """ School age page view. """

    template_name = "school_age.html"
    handle = 'school_age'

class ContactPageView(PageView):
    """ Contact page view. """

    template_name = "contact.html"
    handle = 'contact'

class SubscribePageView(PageView):
    """ Subscribe page view. """

    template_name = "subscribe.html"
    handle = 'subscribe'
