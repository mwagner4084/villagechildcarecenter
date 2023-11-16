import smtplib
from email.mime.text import MIMEText

from django import forms
from django.conf import settings
from django.db import IntegrityError
from django.http import HttpRequest, HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import TemplateView

from django_project import settings

from .forms import ContactForm, InformationRequestForm
from .models import Contact, InformationRequest, Page


class PageView(TemplateView):
    """ Base class for all page views. """
    model = Page
    handle = None
    template_name = ""
    title = ""
    meta_title = "Empowering the Young Minds of Kalamazoo with Quality Childcare"
    description = "Here at The Village, we choose to focus on each individual's strengths rather than their weaknesses. Our childcare philosophy is to provide an age-appropriate environment that develops self-esteem, confidence, and a love of learning."
    keywords = "child care, childcare, day care, daycare, preschool, school age, steam, stem, kalamazoo, portage, oshtemo, vicksburg, mattawan, gull lake, richland, plainwell, paw paw, texas corners, infant care, toddler care, pre-k, pre-kindergarten, kindergarten, before school care, after school care, summer camp, summer care, summer daycare, summer child care, summer childcare, summercamp"
    form = None

    def __init__(self, *args, **kwargs):
        super(PageView, self).__init__(*args, **kwargs)
        if not self.handle or not self.template_name:
            raise Exception('You must define a handle and template_name')

    def get_context_data(self, **kwargs):
        """ Add the page to the context. """
        context = super(PageView, self).get_context_data(**kwargs)
        pages = Page.objects.filter(handle=self.handle)

        if pages:
            page = pages[0]
            context['page'] = page
            context['meta'] = {'title': page.meta_title, 'description': page.description, 'keywords': page.keywords}

        if len(pages):
            context['page'] = pages[0]

        if self.form:
            context['form'] = self.form

        self.context = context

        return context


class HomePageView(PageView):
    """ Home page view. """
    template_name = "index.html"
    form = InformationRequestForm
    handle = 'home'
    title = 'Empowering the Young Minds of Kalamazoo with Quality Childcare'
    
    def __init__(self, *args, **kwargs):
        if not self.handle or not self.template_name:
            raise Exception('You must define a handle and template_name')


    def send_custom_email(self, subject, message, from_email, to_email):
        # Initialize connection
        smtp_server = smtplib.SMTP('smtp.gmail.com', 587)
        smtp_server.starttls()

        email_host_user = settings.EMAIL_HOST_USER
        email_host_password = settings.EMAIL_HOST_PASSWORD
        smtp_server.login(email_host_user, email_host_password)

        # Create email
        msg = MIMEText(message)
        msg['From'] = from_email
        msg['To'] = ', '.join(to_email)
        msg['Subject'] = subject

        # Send email
        smtp_server.sendmail(from_email, to_email, msg.as_string())
        smtp_server.quit()

    def post(self, request: HttpRequest, *args, **kwargs):
        """ Handle the form submission. """

        form = InformationRequestForm(request.POST)
        from_email = 'thevillagechildcarecenter4@gmail.com'
        to_email = ['director@thevillageccc.com', 'mw.devdesign@gmail.com']

        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            sender = settings.DEFAULT_FROM_EMAIL
            recipients = [email]

            # msg.send(fail_silently=False)

            from_email = from_email
            to_email = to_email
            subject = f'New Information Request from {name}'
            message = f'''
                Name: {name}
                Email: {email}
            '''

            try:
                inforequest = InformationRequest.objects.create(
                    name=name,
                    email=email
                )
                inforequest.save()

                self.send_custom_email(subject, message, from_email, to_email)

            except Exception as e:
                context = self.get_context_data(**kwargs)
                error_msg = 'There was an error submitting your request.'
                if isinstance(e, IntegrityError):
                    error_msg = 'This email address has already been submitted.'
                form.add_error(None, forms.ValidationError(error_msg))
                context['form'] = form
                return render(request, self.template_name, context)

            return HttpResponseRedirect('/confirm/')
        else:
            context = self.get_context_data(**kwargs)
            context['form'] = form
            return render(request, self.template_name, context)


class WelcomePageView(PageView):
    """ Welcome page view. """

    template_name = "welcome.html"
    handle = 'philosophy'
    title = 'Welcome to the Village'

class ClassroomPageView(PageView):
    """ Classroom page view. """

    template_name = "classrooms.html"
    handle = 'classrooms'
    title = 'Classrooms'
    

class SteamPageView(PageView):
    """ Steam page view. """

    template_name = "steam.html"
    handle = 'steam'
    title = 'S.T.E.A.M. Room'
    

class PreschoolPageView(PageView):
    """ Preschool page view. """

    template_name = "preschool.html"
    handle = 'preschool'
    title = 'Now Enrolling!'
    

class SchoolAgePageView(PageView):
    """ School age page view. """

    template_name = "school_age.html"
    handle = 'school_age'
    title = 'School Age'
    

class EmploymentPageView(PageView):
    """ Employment page view. """

    template_name = "employment.html"
    handle = 'employment'
    title = 'Employment'
    

class ContactPageView(PageView):
    """ Contact page view. """

    form = ContactForm
    template_name = "contact.html"
    handle = 'contact'
    title = 'Contact Us'
    

    def send_custom_email(self, subject, message, from_email, to_email):
        # Initialize connection
        smtp_server = smtplib.SMTP('smtp.gmail.com', 587)
        smtp_server.starttls()

        email_host_user = settings.EMAIL_HOST_USER
        email_host_password = settings.EMAIL_HOST_PASSWORD
        smtp_server.login(email_host_user, email_host_password)

        # Create email
        msg = MIMEText(message)
        msg['From'] = from_email
        msg['To'] = ', '.join(to_email)
        msg['Subject'] = subject

        # Send email
        smtp_server.sendmail(from_email, to_email, msg.as_string())
        smtp_server.quit()

    def post(self, request: HttpRequest, *args, **kwargs):
        """ Handle the form submission. """

        form = ContactForm(request.POST)
        from_email = 'thevillagechildcarecenter4@gmail.com'
        to_email = ['director@thevillageccc.com', 'mw.devdesign@gmail.com']

        if form.is_valid():
            fname = form.cleaned_data['fname']
            lname = form.cleaned_data['lname']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            children = form.cleaned_data['children']
            start_date = form.cleaned_data['start_date']
            comments = form.cleaned_data['comments']
            referred_by = form.cleaned_data['referred_by']

            # msg.send(fail_silently=False)

            from_email = from_email
            to_email = to_email
            subject = f'New Tour Request from {fname} {lname}'
            message = f'''
                Name: {fname} {lname}
                Email: {email}
                Phone: {phone}
                Children: {children}
                Start Date: {start_date}
                Comments: {comments}
                Referred By: {referred_by}
            '''

            try:
                tour_requests = Contact.objects.create(
                    fname=fname,
                    lname=lname,
                    email=email,
                    phone=phone,
                    children=children,
                    start_date=start_date,
                    comments=comments,
                    referred_by=referred_by,
                )
                tour_requests.save()

                self.send_custom_email(subject, message, from_email, to_email)

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
    title = 'Thank You!'