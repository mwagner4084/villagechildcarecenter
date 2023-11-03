import logging
import smtplib
from email.mime.text import MIMEText

from django import forms
from django.conf import settings
from django.core.mail import EmailMessage
from django.db import IntegrityError
from django.http import HttpRequest, HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import TemplateView

from api.sendgrid import SendGridContact, sendgrid_add_contacts
from django_project import settings

from .forms import ContactForm, InformationRequestForm
from .models import Contact, InformationRequest, Page

logger = logging.getLogger(__name__)


class PageView(TemplateView):
    """ Base class for all page views. """
    model = Page
    handle = None
    template_name = ""
    title = ""
    description = ""
    keywords = ""
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
            context['meta_title'] = page.meta_title
            context['meta_description'] = page.meta_description
            context['meta_keywords'] = page.meta_keywords

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
    title = 'Now Enrolling for 2023 + 2024!'
    description = 'The Village Child Care Center is a locally owned and operated child care center located in the heart of Oshtemo Township. We are committed to providing a safe, nurturing, and educational environment for children ages 6 weeks and up. We are now enrolling for 2023 and 2024!'
    keywords = 'child care, childcare, day care, daycare, preschool, school age, steam, stem, kalamazoo, portage, oshtemo, vicksburg, mattawan, gull lake, richland, plainwell, paw paw, texas corners, infant care, toddler care, pre-k, pre-kindergarten, kindergarten, before school care, after school care, summer camp, summer care, summer daycare, summer child care, summer childcare, summercamp'

    def __init__(self, *args, **kwargs):
        if not self.handle or not self.template_name:
            raise Exception('You must define a handle and template_name')

    def get_context_data(self, **kwargs):
        """ Add the page to the context. """
        context = super(HomePageView, self).get_context_data(**kwargs)
        context['meta_title'] = self.title
        context['meta_description'] = self.description
        context['meta_keywords'] = self.keywords

        if self.form:
            context['form'] = self.form
            context['tag'] = "div"
            context['wrapper_class'] = "form-group"

        self.context = context

        return context

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
    description = 'We believe that children learn best through play and exploration. Our curriculum is designed to foster a love of learning and to prepare children for kindergarten and beyond. We are dedicated to providing a warm and welcoming environment for children and their families. We look forward to welcoming you to the Village!'
    keywords = 'child care, childcare, day care, daycare, preschool, school age, steam, stem, kalamazoo, portage, oshtemo, vicksburg, mattawan, gull lake, richland, plainwell, paw paw, texas corners, infant care, toddler care, pre-k, pre-kindergarten, kindergarten, before school care, after school care, summer camp, summer care, summer daycare, summer child care, summer childcare, summercamp'

    def get_context_data(self, **kwargs):
        context = super(WelcomePageView, self).get_context_data(**kwargs)
        context['meta_title'] = self.title
        context['meta_description'] = self.description
        context['meta_keywords'] = self.keywords

        return context


class ClassroomPageView(PageView):
    """ Classroom page view. """

    template_name = "classrooms.html"
    handle = 'classrooms'
    title = 'Classrooms'
    description = 'We offer programs for children ages 6 weeks and up. Our classrooms are designed to meet the needs of each age group and are equipped with age appropriate toys and materials. We also have a large outdoor play area with a playground and a garden. We are proud to offer a variety of programs to meet the needs of our families.'
    keywords = 'child care, childcare, day care, daycare, preschool, school age, steam, stem, kalamazoo, portage, oshtemo, vicksburg, mattawan, gull lake, richland, plainwell, paw paw, texas corners, infant care, toddler care, pre-k, pre-kindergarten, kindergarten, before school care, after school care, summer camp, summer care, summer daycare, summer child care, summer childcare, summercamp'

    def get_context_data(self, **kwargs):
        context = super(ClassroomPageView, self).get_context_data(**kwargs)
        context['meta_title'] = self.title
        context['meta_description'] = self.description
        context['meta_keywords'] = self.keywords

        return context


class SteamPageView(PageView):
    """ Steam page view. """

    template_name = "steam.html"
    handle = 'steam'
    title = 'S.T.E.A.M. Room'
    description = 'Our S.T.E.A.M. classroom is designed to allow children to use their imagination to explore their creativity.'
    keywords = 'child care, childcare, day care, daycare, preschool, school age, steam, stem, kalamazoo, portage, oshtemo, vicksburg, mattawan, gull lake, richland, plainwell, paw paw, texas corners, infant care, toddler care, pre-k, pre-kindergarten, kindergarten, before school care, after school care, summer camp, summer care, summer daycare, summer child care, summer childcare, summercamp'

    def get_context_data(self, **kwargs):
        context = super(SteamPageView, self).get_context_data(**kwargs)
        context['meta_title'] = self.title
        context['meta_description'] = self.description
        context['meta_keywords'] = self.keywords

        return context


class PreschoolPageView(PageView):
    """ Preschool page view. """

    template_name = "preschool.html"
    handle = 'preschool'
    title = 'Now Enrolling!'
    description = 'Our preschool program is designed to prepare children for kindergarten and beyond. We use the Highscope Curriculum to provide individualized learning focused on nature and science, early math, and logic and reasoning. We offer a creative learning environment that fosters a love of learning.'
    keywords = 'child care, childcare, day care, daycare, preschool, school age, steam, stem, kalamazoo, portage, oshtemo, vicksburg, mattawan, gull lake, richland, plainwell, paw paw, texas corners, infant care, toddler care, pre-k, pre-kindergarten, kindergarten, before school care, after school care, summer camp, summer care, summer daycare, summer child care, summer childcare, summercamp'

    def get_context_data(self, **kwargs):
        context = super(PreschoolPageView, self).get_context_data(**kwargs)
        context['meta_title'] = self.title
        context['meta_description'] = self.description
        context['meta_keywords'] = self.keywords

        return context


class SchoolAgePageView(PageView):
    """ School age page view. """

    template_name = "school_age.html"
    handle = 'school_age'
    title = 'School Age'
    description = 'Our school age program is designed to provide a safe and nurturing environment for children before and after school. We offer transportation to and from local schools and provide a variety of activities to keep children engaged and entertained.'
    keywords = 'child care, childcare, day care, daycare, preschool, school age, steam, stem, kalamazoo, portage, oshtemo, vicksburg, mattawan, gull lake, richland, plainwell, paw paw, texas corners, infant care, toddler care, pre-k, pre-kindergarten, kindergarten, before school care, after school care, summer camp, summer care, summer daycare, summer child care, summer childcare, summercamp'

    def get_context_data(self, **kwargs):
        context = super(SchoolAgePageView, self).get_context_data(**kwargs)
        context['meta_title'] = self.title
        context['meta_description'] = self.description
        context['meta_keywords'] = self.keywords

        return context


class EmploymentPageView(PageView):
    """ Employment page view. """

    template_name = "employment.html"
    handle = 'employment'
    title = 'Employment'
    description = 'We are always looking for talented and dedicated individuals to join our team. If you are interested in joining our team, please fill out the form below and we will contact you to schedule an interview.'
    keywords = 'child care, childcare, day care, daycare, preschool, school age, steam, stem, kalamazoo, portage, oshtemo, vicksburg, mattawan, gull lake, richland, plainwell, paw paw, texas corners, infant care, toddler care, pre-k, pre-kindergarten, kindergarten, before school care, after school care, summer camp, summer care, summer daycare, summer child care, summer childcare, summercamp, employment, jobs, careers, childcare careers, childcare jobs, childcare employment, childcare employer, daycare careers, daycare jobs, kalamazoo jobs, kalamazoo careers, kalamazoo employment'

    def get_context_data(self, **kwargs):
        context = super(EmploymentPageView, self).get_context_data(**kwargs)
        context['meta_title'] = self.title
        context['meta_description'] = self.description
        context['meta_keywords'] = self.keywords

        return context


class ContactPageView(PageView):
    """ Contact page view. """

    form = ContactForm
    template_name = "contact.html"
    handle = 'contact'
    title = 'Contact Us'
    description = 'Please feel free to contact us at any time with any questions or to schedule a tour. We look forward to hearing from you!'
    keywords = 'child care, childcare, day care, daycare, preschool, school age, steam, stem, kalamazoo, portage, oshtemo, vicksburg, mattawan, gull lake, richland, plainwell, paw paw, texas corners, infant care, toddler care, pre-k, pre-kindergarten, kindergarten, before school care, after school care, summer camp, summer care, summer daycare, summer child care, summer childcare, summercamp'

    def get_context_data(self, **kwargs):
        context = super(ContactPageView, self).get_context_data(**kwargs)
        context['meta_title'] = self.title
        context['meta_description'] = self.description
        context['meta_keywords'] = self.keywords

        return context

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
    description = 'Thank you for contacting us! We will be in touch soon!'
    keywords = 'child care, childcare, day care, daycare, preschool, school age, steam, stem, kalamazoo, portage, oshtemo, vicksburg, mattawan, gull lake, richland, plainwell, paw paw, texas corners, infant care, toddler care, pre-k, pre-kindergarten, kindergarten, before school care, after school care, summer camp, summer care, summer daycare, summer child care, summer childcare, summercamp'

    def get_context_data(self, **kwargs):
        context = super(ConfirmPageView, self).get_context_data(**kwargs)
        context['meta_title'] = self.title
        context['meta_description'] = self.description
        context['meta_keywords'] = self.keywords

        return context
