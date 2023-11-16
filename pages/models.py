from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class Page(models.Model):
    """ Page model for static pages. """

    HANDLE_CHOICES = (
        ('home', 'Home'),
        ('philosophy', 'Our Philosophy'),
        ('classrooms', 'Classrooms'),
        ('steam', 'S.T.E.A.M.'),
        ('preschool', 'Preschool'),
        ('school_age', 'School Age'),
        ('contact', 'Contact'),
        ('confirm', 'Confirmation'),
        ('employment', 'Employment Information'),
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
    meta_title = models.CharField(max_length=255, default='Empowering the Young Minds of Kalamazoo with Quality Childcare')
    description = models.TextField(max_length=300, default='Here at The Village, we choose to focus on each individual\'s strengths rather than their weaknesses. Our childcare philosophy is to provide an age-appropriate environment that develops self-esteem, confidence, and a love of learning.')
    keywords = models.TextField(max_length=800, default='childcare, daycare, preschool, school age, kalamazoo, michigan, steam, science, technology, engineering, art, math, education, learning, fun, play, kids, children, infant, toddler, pre-k, pre-k, pre-kindergarten, kindergarten, elementary, after school, before school, summer camp, summer, camp, summer program, summer programs, summer childcare, summer daycare, summer child care, summer day care, summercamp')

    class Meta:
        verbose_name = _("Page")
        verbose_name_plural = _("Pages")
        

    def __str__(self):
        return self.handle


class InformationRequest(models.Model):
    """ Information Request Model """
    name = models.CharField(max_length=254, null=True, blank=True)
    email = models.EmailField(max_length=254, unique=True)
    date_added = models.DateTimeField(auto_now_add=True)
    contacted = models.BooleanField(default=False)
    notes = models.CharField(max_length=5000, null=True, blank=True)

    def __str__(self):
        return f"{self.name}"

    def get_absolute_url(self):
        return reverse("index", args=(self.pk))


class Contact(models.Model):
    """ Contact Model """
    fname = models.CharField(max_length=254, null=True, blank=True)
    lname = models.CharField(max_length=254, null=True, blank=True)
    email = models.EmailField(max_length=254, unique=True)
    phone = models.CharField(max_length=254, null=True, blank=True)
    children = models.CharField(max_length=500, null=True, blank=True)
    start_date = models.DateField(auto_now_add=True)
    comments = models.CharField(max_length=500, null=True, blank=True)
    referred_by = models.CharField(max_length=254, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)
    contacted = models.BooleanField(default=False)
    notes = models.CharField(max_length=5000, null=True, blank=True)

    def __str__(self):
        return f"{self.lname}, {self.fname}"

    def get_absolute_url(self):
        return reverse("contact", args=(self.pk))
