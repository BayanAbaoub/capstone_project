from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Review

# Create your views here.
class ReviewList(generic.ListView):
    queryset = Review.objects.filter(status=1)
    template_name = "blog/index.html"
    paginate_by = 6

def review_detail(request, slug):
    """
    Display an individual :model:`blog.Review`.

    **Context**

    ``post``
        An instance of :model:`blog.Post`.

    **Template:**

    :template:`blog/post_detail.html`
    """

    queryset = Review.objects.filter(status=1)
    review = get_object_or_404(queryset, slug=slug)

    return render(
        request,
        "blog/review_detail.html",
        {"review": review},
    )