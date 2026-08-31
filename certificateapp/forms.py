from django import forms
from .models import CertificateApp


class CertificateForm(forms.ModelForm):
    PROGRAM_CHOICES = [
        ("Computer Engineering", "Computer Engineering"),
        ("Electrical & Electronics Engineering", "Electrical & Electronics Engineering"),
        ("Electrical Engineering", "Electrical Engineering"),
        ("Mechanical Engineering", "Mechanical Engineering"),
        ("Computer Hardware Engineering", "Computer Hardware Engineering"),
        ("Electronics Communication Engineering", "Electronics Communication Engineering"),
    ]

    program_name = forms.ChoiceField(
        choices=PROGRAM_CHOICES,
        widget=forms.Select(attrs={"class": "form-control"}),
        label="Program / Course Name",
    )

    college_name = forms.CharField(
        initial="Model Polytechnic College Karunagappally",
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "readonly": "readonly",
            }
        ),
        label="College Name",
    )

    class Meta:
        model = CertificateApp
        fields = [
            "recipient_name",
            "program_name",
            "college_name",
            "dean_name",
            "issue_date",
        ]

        widgets = {
            "recipient_name": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Recipient Name",
                }
            ),
            "dean_name": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Principal / Dean Name",
                }
            ),
            "issue_date": forms.DateInput(
                attrs={
                    "class": "form-control",
                    "type": "date",
                }
            ),
        }

    def clean_college_name(self):
        return "Model Polytechnic College Karunagappally"
