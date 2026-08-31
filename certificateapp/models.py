from django.db import models
import uuid


COLLEGE_NAME = "Model Polytechnic College Karunagappally"


class CertificateApp(models.Model):
    certificate_id = models.CharField(
        max_length=20,
        unique=True,
        editable=False,
    )
    recipient_name = models.CharField(max_length=150)
    program_name = models.CharField(max_length=200)
    college_name = models.CharField(
        max_length=150,
        default=COLLEGE_NAME,
    )
    principal_name = models.CharField(max_length=150)
    issue_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.certificate_id:
            self.certificate_id = f"CERT-{uuid.uuid4().hex[:8].upper()}"
        # This portal belongs to one college, so always enforce the fixed name.
        self.college_name = COLLEGE_NAME
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.certificate_id} - {self.recipient_name}"
