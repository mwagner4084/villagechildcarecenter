from crispy_bootstrap5.bootstrap5 import FloatingField
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit
from django_recaptcha.fields import ReCaptchaField
from django_recaptcha.widgets import ReCaptchaV2Checkbox
from django import forms


class HomePageForm(forms.ModelForm):
    """ Form for editing the home page. """
    class Meta:
        fields = ['title', 'handle', 'content', 'content_secondary']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 3}),
            'content_secondary': forms.Textarea(attrs={'rows': 3}),
        }


class InformationRequestForm(forms.Form):
    """ Form for the information request page. """
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

    # Honeypot field - hidden from real users
    website = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            'style': 'display:none !important',
            'tabindex': '-1',
            'autocomplete': 'off'
        })
    )

    def clean(self):
        cleaned_data = super().clean()
        # If the honeypot field is filled, it's a bot
        if cleaned_data.get('website'):
            raise forms.ValidationError('Bot submission detected.')
        return cleaned_data

    # captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox())

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-infoReqForm'
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            FloatingField('name'),
            FloatingField('email'),
            # 'captcha',
            Submit('submit', 'Submit')
        )


class ContactForm(forms.Form):
    """ Form for the contact page. """
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

    # Honeypot field - hidden from real users
    website = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            'style': 'display:none !important',
            'tabindex': '-1',
            'autocomplete': 'off'
        })
    )

    def clean(self):
        cleaned_data = super().clean()
        # If the honeypot field is filled, it's a bot
        if cleaned_data.get('website'):
            raise forms.ValidationError('Bot submission detected.')
        return cleaned_data

    # captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox())

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
            # 'captcha',
            Submit('submit', 'Submit')
        )
