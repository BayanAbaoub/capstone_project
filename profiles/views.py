from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import UserProfile
from .forms import UserProfileForm

# Create your views here.

@login_required
def profile_page(request):
    """
    Display user's profile with favourited reviews
    """
    user = request.user
        # Get or create profile if it doesn't exist
    profile, created = UserProfile.objects.get_or_create(user=user)
    favourite_reviews = user.favourite_reviews.filter(status=1).order_by('-created_on')
    
    return render(
        request,
        'profiles/profile.html',
        {
            'profile': profile,
            'favourite_reviews': favourite_reviews,
        }
    )


@login_required
def edit_profile(request):
    """
    Allow users to edit their profile
    """
    profile = get_object_or_404(UserProfile, user=request.user)
    
    if request.method == 'POST':
        # Important: Pass both request.POST and request.FILES to handle image uploads
        form = UserProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully!')
            return redirect('profile')
        else:
            messages.error(request, 'There was an error updating your profile.')
    else:
        form = UserProfileForm(instance=profile)
    
    return render(
        request,
        'profiles/edit_profile.html',
        {'form': form, 'profile': profile}
    )