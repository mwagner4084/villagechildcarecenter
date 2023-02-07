from crispy_bootstrap5.bootstrap5 import FloatingField
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Fieldset, Layout, Submit
from django import forms

from pages.models import Contact, InformationRequest


class HomePageForm(forms.ModelForm):
    """ Form for editing the home page. """
    class Meta:
        fields = ['title', 'handle', 'content', 'content_secondary']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 3}),
            'content_secondary': forms.Textarea(attrs={'rows': 3}),
        }


class InformationRequestForm(forms.Form):
    name = forms.CharField(
        label='Name',
        help_text='',
        max_length=200,
        widget=forms.TextInput()
    )

    email = forms.EmailField(
        label='Email Address',
        max_length=200,
        help_text='',
        widget=forms.EmailInput()
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-infoReqForm'
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            FloatingField('name'),
            FloatingField('email'),
            Submit('submit', 'Submit')
        )


class ContactForm(forms.Form):
    fname = forms.CharField(
        help_text='',
        label='First Name',
        max_length=200,
        widget=forms.TextInput()
    )
    lname = forms.CharField(
        help_text='',
        label='Last Name',
        max_length=200,
        widget=forms.TextInput()
    )
    email = forms.EmailField(
        help_text='',
        label='Email Address',
        max_length=200,
        widget=forms.EmailInput()
    )
    phone = forms.CharField(
        help_text='',
        label='Phone Number',
        max_length=200,
        widget=forms.TextInput()
    )
    children = forms.CharField(
        help_text='',
        label='Children\'s Names and Ages',
        max_length=500,
        widget=forms.TextInput()
    )
    start_date = forms.DateField(
        help_text='',
        label='Start Date (MM/DD/YYYY)',
        widget=forms.DateInput()
    )
    comments = forms.CharField(
        help_text='',
        label='Comments',
        max_length=500,
        widget=forms.TextInput()
    )
    referred_by = forms.CharField(
        help_text='',
        label='How did you hear about us?',
        max_length=200,
        widget=forms.TextInput()
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-contactForm'
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            FloatingField('fname'),
            FloatingField('lname'),
            FloatingField('email'),
            FloatingField('phone'),
            FloatingField('children'),
            FloatingField('start_date'),
            FloatingField('comments'),
            FloatingField('referred_by'),
            Submit('submit', 'Submit')
        )
