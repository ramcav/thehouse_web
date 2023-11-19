from django import forms
from .models import User
from django.core.files.uploadedfile import InMemoryUploadedFile

class JoinWaitlist(forms.ModelForm):
    ...