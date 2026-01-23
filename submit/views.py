from django.shortcuts import render
from django.contrib import messages
from .models import Submit
from .forms import SubmitForm

# Create your views here.



def submit_info(request):
    """
    Renders the Submit page and handles form submissions
    """
    submit = Submit.objects.all().order_by('-updated_on').first()
    
    if request.method == "POST":
        submit_form = SubmitForm(data=request.POST)
        if submit_form.is_valid():
            submit_form.save()
            messages.success(request, 'Thank you! Your review has been submitted successfully.')
            # Create a new empty form after successful submission
            submit_form = SubmitForm()
        else:
            messages.error(request, 'There was an error with your submission. Please check the form.')
    else:
        submit_form = SubmitForm()

    return render(
        request,
        "submit/submit.html",
        {
            "submit": submit,
            "submit_form": submit_form,
        },
    )