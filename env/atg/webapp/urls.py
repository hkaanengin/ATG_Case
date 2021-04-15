from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns
from webapp import views

app_name = "main"   


urlpatterns = [
    path('iataapi/', views.iataapi.as_view(),name="iataapi")
]