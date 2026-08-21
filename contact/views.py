from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import ContactSubmission
from .serializers import ContactSubmissionSerializer
from .tasks import send_enquiry_email, send_enquiry_whatsapp


class ContactSubmissionView(APIView):
    """
    POST /api/contact/
    Saves the submission and triggers background notifications.
    """
    permission_classes = []  # public endpoint, no auth needed

    def post(self, request):
        serializer = ContactSubmissionSerializer(data=request.data)

        if serializer.is_valid():
            submission = serializer.save()

            # .delay() sends task to Celery — runs in background
            # the response is returned immediately without waiting
            send_enquiry_email.delay(submission.id)
            send_enquiry_whatsapp.delay(submission.id)

            return Response(
                {'message': 'Enquiry submitted successfully.'},
                status=status.HTTP_201_CREATED
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)