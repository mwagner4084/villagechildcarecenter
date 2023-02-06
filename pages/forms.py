from django import forms
from pages.models import InformationRequest, Contact

class HomePageForm(forms.ModelForm):
    """ Form for editing the home page. """
    class Meta:
        fields = ['title', 'handle', 'content', 'content_secondary']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 3}),
            'content_secondary': forms.Textarea(attrs={'rows': 3}),
        }

class InformationRequestForm(forms.ModelForm):
    name = forms.CharField(
        label='Your name',
        max_length=200,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    email = forms.EmailField(label='Your email',
        max_length=200,
        help_text='Required',
        widget=forms.EmailInput(attrs={'class': 'form-control'})
    )
    class Meta:
        model = InformationRequest
        fields = ('name', 'email')

    def save(self, commit=True):
        instance = super(InformationRequestForm, self).save(commit=False)
        if commit:
            instance.save()
        return instance

class ContactForm(forms.Form):
    fname = forms.CharField(
        label='Your name',
        max_length=200,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    lname = forms.CharField(
        label='Your name',
        max_length=200,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    email = forms.EmailField(
        label='Your email',
        max_length=200,
        help_text='Required',
        widget=forms.EmailInput(attrs={'class': 'form-control'})
    )
    phone = forms.CharField(
        label='Your phone number',
        max_length=200,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    children = forms.CharField(
        label='Your children',
        max_length=500,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    start_date = forms.DateField(
        label='Start date',
        widget=forms.DateInput(attrs={'class': 'form-control'})
    )
    comments = forms.CharField(
        label='Comments',
        max_length=500,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    referred_by = forms.CharField(
        label='Referred by',
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
