from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
app_name = "theHouse"
urlpatterns = [
    path('', views.LandingView.as_view(), name = "landing"),
    path('waitlist', views.Waitlist.as_view(), name = "waitlist")
]
