from django.db import models


class ContactSubmission(models.Model):
    """
    Stores every enquiry form submission.
    Even if email fails, the data is saved in the database.
    """
    STATUS_CHOICES = [
        ('new', 'New'),
        ('read', 'Read'),
        ('replied', 'Replied'),
    ]

    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True)
    message = models.TextField()

    # optional — which center they enquired about
    center = models.ForeignKey(
        'listings.RehabCenter',
        null=True, blank=True,
        on_delete=models.SET_NULL,  # if center deleted, keep the submission
        related_name='enquiries'
    )

    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='new')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.name} — {self.email}"