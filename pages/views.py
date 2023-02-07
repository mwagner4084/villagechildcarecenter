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
from .models import Contact, InformationRequest, Page


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

    def post(self, request: HttpRequest, *args, **kwargs):
        """ Handle the form submission. """

        form = ContactForm(request.POST)
        if form.is_valid():
            fname = form.cleaned_data['fname']
            lname = form.cleaned_data['lname']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            children = form.cleaned_data['children']
            start_date = form.cleaned_data['start_date']
            comments = form.cleaned_data['comments']
            referred_by = form.cleaned_data['referred_by']
            sender = settings.DEFAULT_FROM_EMAIL
            recipients = [email]

            msg = EmailMessage(from_email=sender, to=recipients)
            msg.template_id = settings.SENDGRID_TEMPLATES.get('contact')
            msg.send(fail_silently=False)

            try:
                schedule_tour = Contact.objects.create(
                    fname=fname,
                    lname=lname,
                    email=email,
                    phone=phone,
                    children=children,
                    start_date=start_date,
                    comments=comments,
                    referred_by=referred_by,
                )
                schedule_tour.save()
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
        # context['form'] = form
        return render(request, self.template_name, context)


class ConfirmPageView(PageView):
    """ Confirmation page view. """

    template_name = "confirm.html"
    handle = 'confirm'


# class ContactFormView(View):
#     """Contact View"""

#     form = ContactForm
#     template_name = "contact.html"
#     success_url = reverse_lazy("confirm")
