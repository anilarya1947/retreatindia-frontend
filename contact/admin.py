from django.contrib import admin
from .models import ContactSubmission


@admin.register(ContactSubmission)
class ContactSubmissionAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone', 'center', 'status', 'created_at']
    list_filter = ['status']
    search_fields = ['name', 'email', 'phone']
    list_editable = ['status']
    readonly_fields = ['name', 'email', 'phone', 'message', 'center', 'created_at']