from django.shortcuts import render, redirect, get_object_or_404
from .forms import CertificateForm
from .models import CertificateApp

def home(request):
    return render(request, "home.html")

def generate_certificate(request):
    if request.method == "POST":
        form = CertificateForm(request.POST)

        if form.is_valid():
            certificate = form.save()

            return redirect(
                "certificateapp:view_certificate",
                certificate_id=certificate.certificate_id,
            )
    else:
        form = CertificateForm()

    return render(
        request,
        "certificate_gen.html",
        {"form": form},
    )


def view_certificate(request, certificate_id):
    cert = get_object_or_404(
        CertificateApp,
        certificate_id=certificate_id,
    )

    return render(
        request,
        "certificate.html",
        {"cert": cert},
    )

def verify_certificate(request):
    certificate = None
    searched = False

    if request.method == "POST":
        certificate_id = request.POST.get("certificate_id", "").strip()
        searched = True

        if certificate_id:
            certificate = CertificateApp.objects.filter(
                certificate_id=certificate_id
            ).first()

    return render(
        request,
        "verify.html",
        {
            "certificate": certificate,
            "searched": searched,
        },
    )