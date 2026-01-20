from . import views
from django.urls import path

urlpatterns = [
    path('', views.submit_info, name='submit'),
]