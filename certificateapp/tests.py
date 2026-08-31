from django.test import TestCase
from django.urls import reverse

from .models import CertificateApp


class CertificatePortalTests(TestCase):

    def test_home_page(self):
        response = self.client.get(reverse("certificateapp:home"))

        self.assertEqual(response.status_code, 200)

    def test_generate_page(self):
        response = self.client.get(
            reverse("certificateapp:generate_certificate")
        )

        self.assertEqual(response.status_code, 200)

    def test_certificate_generation(self):
        response = self.client.post(
            reverse("certificateapp:generate_certificate"),
            {
                "recipient_name": "Test User",
                "program_name": "Diploma in Computer Engineering",
                "college_name": "Model Polytechnic College Karunagappally",
                "dean_name": "Test Dean",
                "registrar_name": "Test Registrar",
                "issue_date": "2026-08-31",
            },
        )

        self.assertEqual(response.status_code, 302)

        certificate = CertificateApp.objects.first()

        self.assertIsNotNone(certificate)
        self.assertEqual(
            certificate.recipient_name,
            "Test User",
        )

    def test_verify_invalid_certificate(self):
        response = self.client.post(
            reverse("certificateapp:verify_certificate"),
            {
                "certificate_id": "INVALID-ID",
            },
        )

        self.assertEqual(response.status_code, 200)
        self.assertContains(
            response,
            "Certificate Not Found",
        )