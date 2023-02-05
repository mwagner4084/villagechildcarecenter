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
# from django.core.mail import send_mail

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

    # handle get request
    def get(self, request, *args, **kwargs):
        form = InformationRequestForm()
        return render(request, self.template_name, {"form": form})

    # handle post request
    def post(self, request, *args, **kwargs):
        form = InformationRequestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("confirm")
        return render(request, self.template_name, {"form": form})

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    @csrf_exempt
    def send_email(request):
        if request.method == 'POST':
            sub = InformationRequest(email=request.POST['email'])
            sub.save()
            message = Mail(
                from_email=settings.DEFAULT_FROM_EMAIL,
                to_emails=sub.email,
                subject='Welcome to The Village!',
                html_content='Thank you for your interest in The Village Childcare Center! \
                We look forward to working with you and your child. \
                We will be in touch soon. \
                '
            )
            sg = SendGridAPIClient(settings.SENDGRID_API_KEY)
            response = sg.send(message)
            return render(request, 'index.html', {'email': sub.email, 'action': 'added', 'form': InformationRequestForm()})
        else:
            return render(request, 'index.html', {'form': InformationRequestForm()})

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

    form_class = ContactForm
    template_name = "contact.html"
    success_url = reverse_lazy("confirm")

    # handle get request
    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {"form": form})

    # handle post request
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect("index")
        return render(request, self.template_name, {"form": form})

    @csrf_exempt
    def new(request):
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
