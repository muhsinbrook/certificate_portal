from datetime import date
from django.shortcuts import render, redirect
from django.contrib import messages

from .models import CertificateApp


def generate_certificate(request):
    if request.method == "POST":
        recipient_name = request.POST.get("recipient_name", "").strip()
        program_name = request.POST.get("program_name", "").strip()
        college_name = request.POST.get("college_name", "Springfield College").strip()
        dean_name = request.POST.get("dean_name", "Dr. Emily Carter").strip()
        registrar_name = request.POST.get("registrar_name", "Dr. Michael Reyes").strip()
        issue_date = request.POST.get("issue_date") or date.today().isoformat()

        if not recipient_name or not program_name:
            messages.error(request, "Please fill in both the recipient name and program name.")
            return render(request, "certificateapp/generate.html")

        cert = CertificateApp.objects.create(
            recipient_name=recipient_name,
            program_name=program_name,
            college_name=college_name or "Springfield College",
            dean_name=dean_name or "Dr. Emily Carter",
            registrar_name=registrar_name or "Dr. Michael Reyes",
            issue_date=issue_date,
        )

        request.session["last_certificate_id"] = cert.certificate_id
        request.session["just_generated"] = True

        return redirect("certificateapp:view_certificate", certificate_id=cert.certificate_id)

    return render(request, "certificateapp/generate.html")


def view_certificate(request, certificate_id):
    try:
        cert = CertificateApp.objects.get(certificate_id=certificate_id)
    except CertificateApp.DoesNotExist:
        messages.error(request, "That certificate could not be found.")
        return redirect("certificateapp:generate_certificate")

    just_generated = request.session.pop("just_generated", False)

    context = {
        "cert": cert,
        "just_generated": just_generated,
    }
    return render(request, "certificateapp/certificate.html", context)