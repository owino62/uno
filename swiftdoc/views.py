from django.shortcuts import render, redirect
from django.core.mail import send_mail, EmailMessage
from django.conf import settings
from .models import ContactRequest

# Create your views here.

def index(request):
    return render(request,'index.html')

def portfolio_details(request):
    return render(request,'portfolio-details.html')

def service_details(request):
    return render(request,'service-details.html')

def work_permits(request):
    return render(request,'work_permits.html')

def class_A(request):
    return render(request, 'class_A.html')

def class_B(request):
    return render(request,'class_B.html')

def class_C(request):
    return render(request, 'class_C.html')

def class_D(request):
    return render(request,'class_D.html')

def class_F(request):
    return render(request,'class_F.html')

def class_G(request):
    return render(request,'class_G.html')

def class_H(request):
    return render(request,'class_H.html')

def class_I(request):
    return render(request,'class_I.html')

def class_K(request):
    return render(request,'class_K.html')

def class_M(request):
    return render(request,'class_M.html')

def immigration_services(request):
    return render(request, 'immigration_services.html')

def first_time(request):
    return render(request,'first_time.html')

def passport_renewal(request):
    return render(request,'passport_renewal.html')

def visa_application(request):
    return render(request,'visa_application.html')

def visa_extension(request):
    return render(request,'visa_extension.html')

def student_pass(request):
    return render(request,'student_pass.html')

def special_pass(request):
    return render(request,'special_pass.html')

def dependent_pass(request):
    return render(request,'dependent_pass.html')

def interstate_pass(request):
    return render(request, 'interstate_pass.html')

def internship_pass(request):
    return render(request,'internship_pass.html')

def application_of_kenyan(request):
    return render(request, 'application_of_kenyan.html')

def regaining_citizenship(request):
    return render(request, 'regaining_citizenship.html')

def declaration_of_dual(request):
    return render(request,'declaration_of_dual.html')

def permanent_residency(request):
    return render(request,'permanent_residency.html')

def marriage_services(request):
    return render(request, 'marriage_services.html')

def birth_certificates(request):
    return render(request, 'birth_certificates.html')

def deed_poll(request):
    return render(request, 'deed_poll.html')

def brs(request):
    return render(request, 'brs.html')

def conveyancing(request):
    return render(request, 'conveyancing.html')

def driving_license(request):
    return render(request, 'driving_license.html')

def eta(request):
    return render(request,'eta.html')

def driving_license(request):
    return render(request,'driving_license.html')


def contact_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        request_text = request.POST.get('request')

        # Save to database
        ContactRequest.objects.create(
            name=name,
            email=email,
            subject=subject,
            request=request_text
        )

         # Send email notification to Zoho inbox
        message = f"Name: {name}\nEmail: {email}\n\nRequest:\n{request_text}"
        mail = EmailMessage(
            subject=f"New Contact Request: {subject}",
            body=message,
            from_email=settings.DEFAULT_FROM_EMAIL,   # your Zoho account
            to=['info@swiftdocx.co.ke'],              # Zoho inbox (business)
            reply_to=[email]                          # customer’s email for reply
        )
        mail.send()

        return render(request, 'index.html',{'sent':True})

    return render(request, 'index.html',{'sent':False})
