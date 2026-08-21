from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings


@shared_task
def send_enquiry_email(submission_id):
    """
    @shared_task means Celery will run this in the background.
    The view triggers this task and immediately returns a response
    without waiting for the email to send.
    """
    from .models import ContactSubmission
    submission = ContactSubmission.objects.get(id=submission_id)

    # Email to admin
    send_mail(
        subject=f'New Enquiry from {submission.name}',
        message=f"""
Name: {submission.name}
Email: {submission.email}
Phone: {submission.phone}
Center: {submission.center.name if submission.center else 'General'}

Message:
{submission.message}
        """,
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=[settings.ADMIN_EMAIL],
        fail_silently=True,  # won't crash if email fails
    )


@shared_task
def send_enquiry_whatsapp(submission_id):
    """
    Placeholder for WhatsApp notification via Twilio or similar.
    Add your WhatsApp API integration here later.
    """
    from .models import ContactSubmission
    submission = ContactSubmission.objects.get(id=submission_id)
    # TODO: integrate Twilio WhatsApp API
    print(f"WhatsApp alert: New enquiry from {submission.name} — {submission.phone}")