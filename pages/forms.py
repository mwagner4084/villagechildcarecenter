from django import forms
from pages.models import InformationRequest, Contact
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Submit
from crispy_bootstrap5.bootstrap5 import FloatingField


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
        self.helper.form_class = 'form-rev-labels'
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            FloatingField('name'),
            FloatingField('email'),
            Submit('submit', 'Submit')
        )

class ContactForm(forms.Form):
    fname = forms.CharField(
        label='',
        help_text='First Name',
        max_length=200,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    lname = forms.CharField(
        label='',
        help_text='Last Name',
        max_length=200,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    email = forms.EmailField(
        label='',
        help_text='Email Address',
        max_length=200,
        widget=forms.EmailInput(attrs={'class': 'form-control'})
    )
    phone = forms.CharField(
        label='',
        help_text='Phone Number',
        max_length=200,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    children = forms.CharField(
        label='',
        help_text='Children\'s Names and Ages',
        max_length=500,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    start_date = forms.DateField(
        label='',
        help_text='Start Date (MM/DD/YYYY)',
        widget=forms.DateInput(attrs={'class': 'form-control'})
    )
    comments = forms.CharField(
        label='',
        help_text='Comments',
        max_length=500,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    referred_by = forms.CharField(
        label='',
        help_text='How did you hear about us?',
        max_length=200,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    class Meta:
        model = Contact
        fields = (
            'fname',
            'lname',
            'email',
            'phone',
            'children',
            'start_date',
            'comments',
            'referred_by',
        )

    def save(self, commit=True):
        contact = Contact(**self.cleaned_data)
        if commit:
            contact.save()
        return contact
