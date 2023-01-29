from django.db import models
# from tinymce import models as tinymce_models
# from tinymce.models import HTMLField

class Page(models.Model):
    HANDLE_CHOICES = (
        ('home', 'Home'),
        ('philosophy', 'Our Philosophy'),
        ('classrooms', 'Classrooms'),
        ('steam', 'S.T.E.A.M.'),
        ('preschool', 'Preschool'),
        ('school_age', 'School Age'),
        ('contact', 'Contact'),
    )

    handle = models.CharField(
        choices=HANDLE_CHOICES,
        blank=False,
        null=True,
        max_length=200,
    )
    title = models.CharField(max_length=200, default='Title')
    content = models.CharField(max_length=500000, default='Content')
    content_secondary = models.CharField(max_length=500000, default='Content2')

    def __str__(self):
        return self.handle
