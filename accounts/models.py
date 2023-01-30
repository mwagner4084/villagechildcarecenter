from django.db import models
from django.urls import reverse
import django.contrib.auth.models
import django.contrib.auth.validators
from django.contrib.auth.models import AbstractUser
import django.utils.timezone
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from pages.models import Page

class CustomUser(AbstractUser):
    """ Custom User Model """

    email = models.EmailField(
        blank=True,
        unique=True,
        max_length=254,
        verbose_name='email address'
    )
    username = models.CharField(
        error_messages={'unique': 'A user with that username already exists.'},
        help_text='\nRequired. 150 characters or fewer. Letters, digits and @/./+/-/_ only.',
        max_length=150,
        unique=True,
        validators=[django.contrib.auth.validators.UnicodeUsernameValidator()],
        verbose_name='username'
    )
    last_login = models.DateTimeField(default=django.utils.timezone.now)

    # all user to login with email
    USERNAME_FIELD = 'username'
    # username required by default
    REQUIRED_FIELDS = ['password']

    def save(self, *args, **kwargs):
        if not self.id:
            self.date_joined = timezone.now()
        self.last_login = timezone.now()
        return super(CustomUser, self).save(*args, **kwargs)

    def __str__(self):
        """ Return string representation of user """
        if self.username == None:
            return "ERROR - USERNAME IS NULL."
        return f"{self.username}"

    def get_absolute_url(self):
        return reverse("login", args=(self.pk))
