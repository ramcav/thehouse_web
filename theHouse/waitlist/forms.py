from django import forms
from .models import UserSubmission
from django.core.files.uploadedfile import InMemoryUploadedFile

class UserSubmissionForm(forms.ModelForm):
    class Meta:
        model = UserSubmission
        fields = ['email', 'username']