from django.urls import path
from list.views import download_pdf

urlpatterns = [
    path('', download_pdf, name='download_pdf'),
]
