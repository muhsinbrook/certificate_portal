from django import forms
from .models import CertificateApp


class CertificateForm(forms.ModelForm):
    class Meta:
        model = CertificateApp
        fields = [
            "recipient_name",
            "program_name",
            "college_name",
            "dean_name",
            "registrar_name",
            "issue_date",
        ]

        widgets = {
            "recipient_name": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Jane A. Doe",
                }
            ),

            "program_name": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Bachelor of Science in Computer Science",
                }
            ),

            "college_name": forms.TextInput(
                attrs={
                    "class": "form-control",
                }
            ),

            "dean_name": forms.TextInput(
                attrs={
                    "class": "form-control",
                }
            ),

            "registrar_name": forms.TextInput(
                attrs={
                    "class": "form-control",
                }
            ),

            "issue_date": forms.DateInput(
                attrs={
                    "class": "form-control",
                    "type": "date",
                }
            ),
        }