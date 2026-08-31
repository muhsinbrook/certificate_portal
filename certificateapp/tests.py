from datetime import date

from django.test import TestCase
from django.urls import reverse

from .models import COLLEGE_NAME, CertificateApp


class CertificatePortalTests(TestCase):
    def test_home_page(self):
        response = self.client.get(reverse("certificateapp:home"))
        self.assertEqual(response.status_code, 200)

    def test_generate_page(self):
        response = self.client.get(
            reverse("certificateapp:generate_certificate")
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Program / Course Name")
        self.assertContains(response, "Principal Name")
        self.assertNotContains(response, "Registrar Name")
        self.assertContains(response, COLLEGE_NAME)

    def test_generate_page_uses_course_choices(self):
        response = self.client.get(
            reverse("certificateapp:generate_certificate")
        )
        self.assertContains(response, "Computer Engineering")
        self.assertContains(response, "Electrical &amp; Electronics Engineering")
        self.assertContains(response, "Mechanical Engineering")

    def test_certificate_generation(self):
        response = self.client.post(
            reverse("certificateapp:generate_certificate"),
            {
                "recipient_name": "Test User",
                "program_name": "Computer Engineering",
                "college_name": COLLEGE_NAME,
                "principal_name": "Test Principal",
                "issue_date": "2026-08-31",
            },
        )

        self.assertEqual(response.status_code, 302)
        certificate = CertificateApp.objects.get(recipient_name="Test User")
        self.assertEqual(certificate.program_name, "Computer Engineering")
        self.assertEqual(certificate.college_name, COLLEGE_NAME)
        self.assertEqual(certificate.principal_name, "Test Principal")
        self.assertEqual(certificate.issue_date, date(2026, 8, 31))
        self.assertFalse(hasattr(certificate, "registrar_name"))

    def test_invalid_program_is_rejected(self):
        response = self.client.post(
            reverse("certificateapp:generate_certificate"),
            {
                "recipient_name": "Test User",
                "program_name": "Not A Real Course",
                "college_name": COLLEGE_NAME,
                "principal_name": "Test Principal",
                "issue_date": "2026-08-31",
            },
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(CertificateApp.objects.count(), 0)

    def test_college_name_is_always_fixed(self):
        certificate = CertificateApp.objects.create(
            recipient_name="Test User",
            program_name="Computer Engineering",
            college_name="Wrong College",
            principal_name="Test Principal",
            issue_date="2026-08-31",
        )
        certificate.refresh_from_db()
        self.assertEqual(certificate.college_name, COLLEGE_NAME)

    def test_view_certificate_page(self):
        certificate = CertificateApp.objects.create(
            recipient_name="Test User",
            program_name="Computer Engineering",
            college_name=COLLEGE_NAME,
            principal_name="Test Principal",
            issue_date="2026-08-31",
        )
        response = self.client.get(
            reverse(
                "certificateapp:view_certificate",
                args=[certificate.certificate_id],
            )
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test User")
        self.assertContains(response, "Test Principal")
        self.assertNotContains(response, "Registrar")

    def test_verify_invalid_certificate(self):
        response = self.client.post(
            reverse("certificateapp:verify_certificate"),
            {"certificate_id": "INVALID-ID"},
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Certificate Not Found")

    def test_verify_valid_certificate(self):
        certificate = CertificateApp.objects.create(
            recipient_name="Test User",
            program_name="Computer Engineering",
            college_name=COLLEGE_NAME,
            principal_name="Test Principal",
            issue_date="2026-08-31",
        )
        response = self.client.post(
            reverse("certificateapp:verify_certificate"),
            {"certificate_id": certificate.certificate_id},
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Certificate Valid")
        self.assertContains(response, certificate.certificate_id)
