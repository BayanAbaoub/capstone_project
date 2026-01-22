from django import forms
from .models import UserProfile


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['bio', 'profile_picture']
        widgets = {
            'bio': forms.Textarea(attrs={'rows': 4, 'class': 'form-control'}),
            'profile_picture': forms.FileInput(attrs={'class': 'form-control'}), 
        }
        labels = {
            'bio': 'Biography',
            'profile_picture': 'Profile Picture'
        }
        help_texts = {
            'profile_picture': 'Upload a profile picture (optional)'
        }