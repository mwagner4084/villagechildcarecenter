from django.db import models
from tinymce.models import HTMLField

class Homepage(models.Models):
    title = models.CharField(max_length=200)
    content = HTMLField()
    #image = models.ImageField()