from django.urls import path
from . import views

app_name = "thehouse"
urlpatterns = [
    path('', views.LandingView.as_view(), name="landing"),
    path('waitlist/', views.LandingView.as_view(), name="waitlist")
]