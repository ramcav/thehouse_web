from django.shortcuts import render
from django.conf import settings
from django.views import View
from .forms import UserSubmissionForm

class LandingView(View):
    def get(self, request, *args, **kwargs):
        form = UserSubmissionForm()
        return render(request, 'website/landing.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = UserSubmissionForm(request.POST)
        if form.is_valid():
            # Save the form and do something specific for 'waitlist'
            submission = form.save(commit=False)
            # You can add additional processing here if necessary
            submission.save()
            # Redirect to the same page with a success message
            return render(request, 'website/landing.html', {
                'form': UserSubmissionForm(),  # Provide a fresh form
                'success': True  # Add success flag for the popup message
            })
        else:
            # If the form is not valid, render the page with the form errors
            return render(request, 'website/landing.html', {'form': form})
            
