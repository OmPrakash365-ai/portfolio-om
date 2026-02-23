from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.core.mail import send_mail
from django.conf import settings
from .serializers import ContactSerializer


@api_view(['POST'])
def contact_api(request):
    serializer = ContactSerializer(data=request.data)

    if serializer.is_valid():
        contact = serializer.save()

        # EMAIL TO ADMIN
        send_mail(
            subject=f"New Message from {contact.name}",
            message=contact.message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[settings.EMAIL_HOST_USER],
            fail_silently=False   # IMPORTANT
        )

        # EMAIL TO USER
        send_mail(
            subject="Thank you for contacting me",
            message="We received your message.",
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[contact.email],
            fail_silently=False   # IMPORTANT
        )

        return Response({"message": "Saved + Email sent"})

    return Response(serializer.errors)