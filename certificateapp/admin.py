from django.contrib import admin

from .models import CertificateApp


@admin.register(CertificateApp)
class CertificateAppAdmin(admin.ModelAdmin):
    list_display = (
        "certificate_id",
        "recipient_name",
        "program_name",
        "principal_name",
        "issue_date",
    )
    search_fields = (
        "certificate_id",
        "recipient_name",
        "program_name",
        "principal_name",
    )
    list_filter = ("program_name", "issue_date")
    readonly_fields = ("certificate_id", "college_name", "created_at")
