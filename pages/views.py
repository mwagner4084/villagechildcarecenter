from django import forms
from django.conf import settings
from django.core.mail import EmailMessage
from django.db import IntegrityError
from django.http import HttpRequest, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, View

from django_project import settings

from .forms import ContactForm, InformationRequestForm
from .models import InformationRequest, Page


class PageView(TemplateView):
    """ Base class for all page views. """
    model = Page
    handle = None
    template_name = None
    form = None

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

        if self.form:
            context['form'] = self.form

        self.context = context

        return context


class HomePageView(PageView):
    """ Home page view. """
    template_name = "index.html"
    handle = 'home'
    form = InformationRequestForm

    def post(self, request: HttpRequest, *args, **kwargs):
        """ Handle the form submission. """

        form = InformationRequestForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            sender = settings.DEFAULT_FROM_EMAIL
            recipients = [email]

            msg = EmailMessage(from_email=sender, to=recipients)
            msg.template_id = settings.SENDGRID_TEMPLATES.get('info_request')
            msg.send(fail_silently=False)

            try:
                inforequest = InformationRequest.objects.create(
                    name=name,
                    email=email
                )
                inforequest.save()
            except Exception as e:
                context = self.get_context_data(**kwargs)
                error_msg = 'There was an error submitting your request.'
                if isinstance(e, IntegrityError):
                    error_msg = 'This email address has already been submitted.'
                form.add_error(None, forms.ValidationError(error_msg))
                context['form'] = form
                return render(request, self.template_name, context)

            return HttpResponseRedirect('/confirm/')

        context = self.get_context_data(**kwargs)
        context['form'] = form
        return render(request, self.template_name, context)


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
    form = ContactForm


class ConfirmPageView(PageView):
    """ Confirmation page view. """

    template_name = "confirm.html"
    handle = 'confirm'

# send_mail('Subject here', 'Here is the message.', 'from@example.com', ['to@example.com'], fail_silently=False)

# class InformationRequestView(View):
#     """Email View"""

#     form_class = InformationRequestForm
#     template_name = "index.html"
#     success_url = reverse_lazy("confirm")

#     # handle get request
#     def get(self, request, *args, **kwargs):
#         form = self.form_class()
#         return render(request, self.template_name, {"form": form})

#     # handle post request
#     def post(self, request, *args, **kwargs):
#         form = self.form_class(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect("index")
#         return render(request, self.template_name, {"form": form})

#     def form_valid(self, form):
#         form.save()
#         return super().form_valid(form)


class ContactFormView(View):
    """Contact View"""

    form = ContactForm
    template_name = "contact.html"
    success_url = reverse_lazy("confirm")
