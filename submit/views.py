from django.shortcuts import render
from .models import Submit

# Create your views here.



def submit_info(request):
    """
    Renders the Submit page
    """
    submit = Submit.objects.all().order_by('-updated_on').first()

    return render(
        request,
        "submit/submit.html",
        {"submit": submit},
    )