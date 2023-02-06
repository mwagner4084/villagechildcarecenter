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
from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


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

class ExampleForm(forms.Form):
    like_website = forms.TypedChoiceField(
        label = "Do you like this website?",
        choices = ((1, "Yes"), (0, "No")),
        coerce = lambda x: bool(int(x)),
        widget = forms.RadioSelect,
        initial = '1',
        required = True,
    )

    favorite_food = forms.CharField(
        label = "What is your favorite food?",
        max_length = 80,
        required = True,
    )

    favorite_color = forms.CharField(
        label = "What is your favorite color?",
        max_length = 80,
        required = True,
    )

    favorite_number = forms.IntegerField(
        label = "Favorite number",
        required = False,
    )

    notes = forms.CharField(
        label = "Additional notes or feedback",
        required = False,
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-exampleForm'
        self.helper.form_class = 'blueForms'
        self.helper.form_method = 'post'

        self.helper.add_input(Submit('submit', 'Submit'))

class HomePageView(PageView):
    """ Home page view. """

    template_name = "index.html"
    handle = 'home'
    form = ExampleForm()


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
