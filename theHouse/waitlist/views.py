import os

from django.shortcuts import render, redirect
from django.conf import settings
from django.views import View
from django.http import FileResponse, Http404
from django.utils.safestring import mark_safe
from django.contrib.staticfiles import finders

from .forms import UserSubmissionForm
from .models import UserSubmission

class LandingView(View):
    def get(self, request, *args, **kwargs):
        form = UserSubmissionForm()
        return render(request, 'waitlist/landing.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = UserSubmissionForm(request.POST)
        print(form)
        if form.is_valid():
            # Extract the username from the form
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')

            # Check if a user with this username already exists
            if UserSubmission.objects.filter(username=username).exists():
                # Handle the case where the username already exists
                # You can add an error message to the form or context here
                print("username already exists")
                return render(request, 'waitlist/landing.html', {
                    'form': form, 
                    'error': 'This username is already stashed! 😯',
                    'button_message': 'stash another one'})
            
            elif UserSubmission.objects.filter(email=email).exists():
                print("email already exists")
                
                error_message = mark_safe("We already stashed a username for you! You'll hear from us soon 👀")
                
                return render(request, 'waitlist/landing.html', {
                'form': form, 
                'error': error_message, 
                'button_message':'go back'
            })

            # Save the form since the username is unique
            submission = form.save(commit=False)
            # Additional processing if necessary
            submission.save()

            
            print("success")
            # Redirect to success page
            return redirect("/success")
    
        else:
            print(form.errors)
            # Form is not valid, render the page with form errors
            return render(request, 'waitlist/landing.html', {'form': form})
        
class Confirmation(View):
    def get(self, request):
        return render(request, 'waitlist/confirmation.html')
            
def terms_of_service_pdf(request):
    pdf_filename = 'terms.pdf'
    if settings.DEBUG:
        pdf_path = finders.find('waitlist/pdfs/' + pdf_filename)
    else:
        pdf_path = os.path.join(settings.STATIC_ROOT, 'waitlist/pdfs', pdf_filename)

    if pdf_path is not None:
        try:
            return FileResponse(open(pdf_path, 'rb'), content_type='application/pdf')
        except FileNotFoundError:
            raise Http404('The requested pdf was not found in our server.')
    else:
        raise Http404('The requested pdf was not found in our server.')

def privacy_policy_pdf(request):
    pdf_filename = 'privacy.pdf'
    if settings.DEBUG:
        pdf_path = finders.find('waitlist/pdfs/' + pdf_filename)
    else:
        pdf_path = os.path.join(settings.STATIC_ROOT, 'waitlist/pdfs', pdf_filename)

    if pdf_path is not None:
        try:
            return FileResponse(open(pdf_path, 'rb'), content_type='application/pdf')
        except FileNotFoundError:
            raise Http404('The requested pdf was not found in our server.')
    else:
        raise Http404('The requested pdf was not found in our server.')