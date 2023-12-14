from django.urls import path
from . import views

app_name = "thehouse"
urlpatterns = [
    path('', views.LandingView.as_view(), name="landing"),
    path('success/', views.Confirmation.as_view(), name="waitlist"),
    path('terms-of-service/', views.terms_of_service_pdf, name='terms'),
    path('privacy-policy/', views.privacy_policy_pdf, name='privacy'),
]
