from django.contrib import admin
from .models import Submit
from django_summernote.admin import SummernoteModelAdmin


# Register your models here.

@admin.register(Submit)
class SubmitAdmin(SummernoteModelAdmin):

    summernote_fields = ('content',)