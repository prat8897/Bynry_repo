from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class ServiceRequest(models.Model):
    SERVICE_TYPES = (
        ('Type 1', 'Type 1'),
        ('Type 2', 'Type 2'),
        # Add more service types as needed
    )

    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('done', 'Done'),
    )

    type = models.CharField(max_length=50, choices=SERVICE_TYPES)
    details = models.TextField()
    attached_files = models.FileField(upload_to='service_request_attachments/', blank=True, null=True)
    submitted_datetime = models.DateTimeField(auto_now_add=True)
    resolved_datetime = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    user = models.ForeignKey(User, on_delete=models.CASCADE)


    def save(self, *args, **kwargs):
        if self.status == 'done' and not self.resolved_datetime:
            self.resolved_datetime = timezone.now()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.type} - {self.status}"

class RequestTracking(models.Model):
    service_request = models.ForeignKey(ServiceRequest, on_delete=models.CASCADE)
    status = models.CharField(max_length=50)
    datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.service_request}: {self.status} at {self.datetime}"
