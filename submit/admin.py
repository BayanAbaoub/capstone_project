from django.contrib import admin
from .models import Submit, SubmitRequest
from django_summernote.admin import SummernoteModelAdmin


# Register your models here.

@admin.register(Submit)
class SubmitAdmin(SummernoteModelAdmin):

    summernote_fields = ('content',)

@admin.register(SubmitRequest)
class SubmitRequestAdmin(admin.ModelAdmin):

    list_display = ('submission', 'read',)



