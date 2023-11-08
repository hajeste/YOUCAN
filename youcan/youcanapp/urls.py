from django.urls import path

from youcanapp import views
from youcanapp.views import *

urlpatterns = [
    path('', index, name='home'),
    path('submit_application/', submit_application, name='submit_application'),
]

