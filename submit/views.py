from django.shortcuts import render
from .models import Submit
from .forms import SubmitForm

# Create your views here.



def submit_info(request):
    """
    Renders the Submit page
    """
    submit = Submit.objects.all().order_by('-updated_on').first()
    submit_form = SubmitForm()


    return render(
        request,
        "submit/submit.html",
        {
            "submit": submit,
            "submit_form": submit_form,
        },
    )