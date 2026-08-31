from django.db import models
import uuid


class CertificateApp(models.Model):
    certificate_id = models.CharField(
        max_length=20, unique=True, editable=False
    )
    recipient_name = models.CharField(max_length=150)
    program_name = models.CharField(max_length=200)
    college_name = models.CharField(max_length=150, default="Springfield College")
    dean_name = models.CharField(max_length=150, default="Dr. Emily Carter")
    registrar_name = models.CharField(max_length=150, default="Dr. Michael Reyes")
    issue_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.certificate_id:
            self.certificate_id = f"CERT-{uuid.uuid4().hex[:8].upper()}"
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.certificate_id} - {self.recipient_name}"