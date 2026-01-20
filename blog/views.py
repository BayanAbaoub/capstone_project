from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .models import Review, Comment
from .forms import CommentForm

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
    comments = review.comments.all().order_by("-created_on")
    comment_count = review.comments.filter(approved=True).count()
    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.review = review
            comment.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Comment submitted and awaiting approval'
            )

    comment_form = CommentForm()

    return render(
        request,
        "blog/review_detail.html",
        {"review": review, "comments": comments, "comment_count": comment_count, "comment_form": comment_form},
    )

def comment_edit(request, slug, comment_id):
    """
    view to edit comments
    """
    if request.method == "POST":

        queryset = Review.objects.filter(status=1)
        review = get_object_or_404(queryset, slug=slug)
        comment = get_object_or_404(Comment, pk=comment_id)
        comment_form = CommentForm(data=request.POST, instance=comment)

        if comment_form.is_valid() and comment.author == request.user:
            comment = comment_form.save(commit=False)
            comment.review = review
            comment.approved = False
            comment.save()
            messages.add_message(request, messages.SUCCESS, 'Comment Updated!')
        else:
            messages.add_message(request, messages.ERROR, 'Error updating comment!')

    return HttpResponseRedirect(reverse('review_detail', args=[slug]))

def comment_delete(request, slug, comment_id):
    """
    view to delete comment
    """
    queryset = Review.objects.filter(status=1)
    review = get_object_or_404(queryset, slug=slug)
    comment = get_object_or_404(Comment, pk=comment_id)

    if comment.author == request.user:
        comment.delete()
        messages.add_message(request, messages.SUCCESS, 'Comment deleted!')
    else:
        messages.add_message(request, messages.ERROR, 'You can only delete your own comments!')

    return HttpResponseRedirect(reverse('review_detail', args=[slug]))

@login_required
def review_favourite(request, slug):
    """
    Toggle favourite status for a review
    """
    review = get_object_or_404(Review, slug=slug)
    
    if review.favourites.filter(id=request.user.id).exists():
        review.favourites.remove(request.user)
        messages.add_message(request, messages.SUCCESS, 'Removed from favourites')
    else:
        review.favourites.add(request.user)
        messages.add_message(request, messages.SUCCESS, 'Added to favourites')
    
        # Redirect back to the page the user came from
    # If no referrer, default to review detail page
    next_url = request.META.get('HTTP_REFERER')
    if next_url and '/profile/' in next_url:
        return HttpResponseRedirect(reverse('profile'))
    else:
        return HttpResponseRedirect(reverse('review_detail', args=[slug]))