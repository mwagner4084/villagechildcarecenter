from django.db import models

class HTMLModel(models.Model):
    page_name = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    content = models.TextField()

    def __str__(self):
        return self.page_name