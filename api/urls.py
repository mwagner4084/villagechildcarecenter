from django.urls import path
from . import views
urlpatterns = [
    path('upload_image/', views.upload_image),
    path('submit_contact/', views.submit_contact),
]
