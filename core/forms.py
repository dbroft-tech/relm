from django import forms
from .models import PrayerRequest, Donation

class PrayerRequestForm(forms.ModelForm):
    class Meta:
        model = PrayerRequest
        fields = ['name', 'email', 'request', 'is_private']
        widgets = {
            'request': forms.Textarea(attrs={'rows': 4}),
        }

class DonationForm(forms.ModelForm):
    class Meta:
        model = Donation
        fields = ['name', 'email', 'amount']

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    subject = forms.CharField(max_length=200)
    message = forms.CharField(widget=forms.Textarea)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Add Bootstrap classes and custom styling
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control',
                'placeholder': f'Enter your {field}'
            }) 