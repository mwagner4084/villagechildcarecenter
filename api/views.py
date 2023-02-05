import os

from django.conf import settings
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpRequest, JsonResponse, HttpResponse
from django.shortcuts import render, redirect
from pages.forms import InformationRequestForm, ContactForm

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


