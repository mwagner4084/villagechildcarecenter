from django import forms

class HomePageForm(forms.ModelForm):
    class Meta:
        fields = ['title', 'handle', 'content', 'image']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 3}),
        }