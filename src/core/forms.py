from django import forms
from .models import Services, Contact
from django_summernote.widgets import SummernoteWidget


class ServicesForm(forms.ModelForm):
    # content = forms.CharField(widget=SummernoteWidget())  # instead of forms.Textarea

    class Meta:
        model = Services
        fields = '__all__'


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'
