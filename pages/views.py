from django.views.generic import View, TemplateView
from .models import Page, InformationRequest, Contact
from .forms import InformationRequestForm, ContactForm
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from django.conf import settings
from django_project import settings
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpRequest, JsonResponse, HttpResponse
from django.core.mail import send_mail, BadHeaderError

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

TEMPLATE_ID = 'd-e1123576e9594830abb7a8fca73b0dc6'
class HomePageView(PageView):
    """ Home page view. """

    template_name = "index.html"
    handle = 'home'
    form = InformationRequestForm()

    # handle get request
    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        return render(request=request, template_name=self.template_name, context=context)

    # handle post request
    def post(self, request, *args, **kwargs):
        form = InformationRequestForm(request.POST)
        if form.is_valid():
            subject = 'Welcome to the village!'
            from_email = settings.DEFAULT_FROM_EMAIL
            to_email = [form.cleaned_data.get('email')]
            message = form.cleaned_data['message']
            form.save()
            try:
                send_mail(subject, message, from_email, to_email, fail_silently=False)
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect("confirm")
        context = self.get_context_data(**kwargs)
        return render(request=request, template_name=self.template_name, context=context)

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    @csrf_exempt
    def send_email(request: HttpRequest) -> HttpResponse:
        '''Send email to the user'''
        if request.method == 'POST':
            sub = InformationRequest(email=request.POST['email'], name=request.POST['name'])
            sub.save()
            message = Mail(
                from_email=settings.DEFAULT_FROM_EMAIL,
                to_emails=sub.email)
            message.dynamic_template_data = {
                'subject': 'Thank you for subscribing',
                'name': sub.name,
                'email': sub.email
                }
            message.template_id = TEMPLATE_ID
            try:
                sg = SendGridAPIClient(settings.SENDGRID_API_KEY)
                response = sg.send(message)
                code, body, headers = response.status_code, response.body, response.headers
                print(f"Response code: {code}")
                print(f"Response body: {body}")
                print(f"Response headers: {headers}")
                print("Dynamic template data sent!")
                return HttpResponse('Email sent')
            except Exception as e:
                # print(e.message)
                print("Error: {0}".format(e))
            return str(response.status_code)
            # return HttpResponse('Email not sent')
        # return HttpResponse('Wrong request')

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

    # handle get request
    def get(self, request, *args, **kwargs):
        form = self.form()
        return render(request, self.template_name, {"form": form})

    # handle post request
    def post(self, request, *args, **kwargs):
        form = self.form(request.POST)
        if form.is_valid():
            form.save()
            return redirect("index")
        return render(request, self.template_name, {"form": form})

    @csrf_exempt
    def send_email(request: HttpRequest):
        if request.method == 'POST':
            sub = Contact(email=request.POST['email'])
            sub.save()
            message = Mail(
                from_email=settings.DEFAULT_FROM_EMAIL,
                to_emails=sub.email,
                subject='The Village Childcare Center Confirmation',
                html_content='Thank you for your interest in The Village Childcare Center! \
                    Verify your email here: \
                    <a href="{}/confirm/?email={}&conf_num={}"> clicking here to \
                    confirm your registration</a>.'.format(request.build_absolute_uri('/confirm/'),
                                                        sub.email))
            sg = SendGridAPIClient(settings.SENDGRID_API_KEY)
            response = sg.send(message)
            return render(request, 'contact.html', {'email': sub.email, 'action': 'added', 'form': ContactForm()})
        else:
            return render(request, 'contact.html', {'form': ContactForm()})
