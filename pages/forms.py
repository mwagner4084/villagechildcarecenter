from django import forms

class HomePageForm(forms.ModelForm):
    class Meta:
        fields = ['title', 'handle', 'content', 'content_secondary']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 3}),
            'content_secondary': forms.Textarea(attrs={'rows': 3}),
        }
