from django.shortcuts import render

# Create your views here.
from .models import ContactMessage
from django.core.mail import send_mail
from django.conf import settings

 
def contact_view(request):
    success = False

    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']

        # Save to DB
        ContactMessage.objects.create(
            name=name,
            email=email,
            message=message
        )

        # Send email to admin
        send_mail(
            subject=f"New Contact Message from {name}",
            message=message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[settings.EMAIL_HOST_USER],
        )

        # Send confirmation email to user
        send_mail(
            subject="Thank you for contacting me",
            message="We received your message. I will contact you soon.",
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[email],
        )

        success = True

    return render(request, 'contact/contact.html', {'success': success})
