import os

from django.conf import settings
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

from django_project import settings
from pages.forms import ContactForm, InformationRequestForm
from pages.models import Contact, InformationRequest


@csrf_exempt
def upload_image(request: HttpRequest) -> JsonResponse:
    if request.method == "POST":
        file_obj = request.FILES['file']
        file_name_suffix = file_obj.name.split(".")[-1]
        if file_name_suffix not in ["jpg", "png", "gif", "jpeg", ]:
            return JsonResponse({"message": "Wrong file format"})

        path = os.path.join(
            settings.MEDIA_ROOT,
            'tinymce',
        )
        # If there is no such path, create
        if not os.path.exists(path):
            os.makedirs(path)

        file_path = os.path.join(path, file_obj.name)

        file_url = f'{settings.MEDIA_URL}tinymce/{file_obj.name}'

        if os.path.exists(file_path):
            return JsonResponse({
                "message": "file already exist",
                'location': file_url
            })

        with open(file_path, 'wb+') as f:
            for chunk in file_obj.chunks():
                f.write(chunk)

        return JsonResponse({
            'message': 'Image uploaded successfully',
            'location': file_url
        })
    return JsonResponse({'detail': "Wrong request"})


@csrf_exempt
def submit_contact(request: HttpRequest) -> HttpResponse:
    '''Submit contact form and rediret to the confirmation page'''
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('confirm')
        return render(request, 'contact.html', {'form': form})
    return HttpResponse('Wrong request')


@csrf_exempt
def submit_information_request(request: HttpRequest) -> HttpResponse:
    '''Submit information request form and rediret to the confirmation page'''
    if request.method == 'POST':
        form = InformationRequestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('confirm')
        return render(request, 'index.html', {'form': form})
    return HttpResponse('Wrong request')


TEMPLATE_ID = 'd-e1123576e9594830abb7a8fca73b0dc6'


@csrf_exempt
def send_email(request: HttpRequest) -> HttpResponse:
    '''Send email to the user'''
    if request.method == 'POST':
        sub = InformationRequest(
            email=request.POST['email'], name=request.POST['name'])
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
