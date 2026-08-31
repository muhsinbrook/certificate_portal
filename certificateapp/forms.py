from django import forms

from .models import COLLEGE_NAME, CertificateApp


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
        initial=COLLEGE_NAME,
        disabled=True,
        widget=forms.TextInput(attrs={"class": "form-control"}),
        label="College Name",
    )

    principal_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Principal Name",
                "autocomplete": "name",
            }
        ),
        label="Principal Name",
        max_length=150,
    )

    class Meta:
        model = CertificateApp
        fields = [
            "recipient_name",
            "program_name",
            "college_name",
            "principal_name",
            "issue_date",
        ]
        widgets = {
            "recipient_name": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Recipient Name",
                    "autocomplete": "name",
                }
            ),
            "issue_date": forms.DateInput(
                format="%Y-%m-%d",
                attrs={
                    "class": "form-control",
                    "type": "date",
                },
            ),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["college_name"].initial = COLLEGE_NAME
        self.fields["issue_date"].input_formats = ["%Y-%m-%d"]

    def clean_college_name(self):
        return COLLEGE_NAME
