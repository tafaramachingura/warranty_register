
        # warranty_api/models.py
from django.db import models
from django.contrib.auth.models import User

class Asset(models.Model):
    asset_id = models.CharField(max_length=100, unique=True,)
    asset_name = models.CharField(max_length=255)
    serial_number = models.CharField(max_length=100)
    purchase_date = models.DateField()
    warranty_start = models.DateField(null=True, blank=True)
    warranty_end = models.DateField(null=True, blank=True)
    registered_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    registrant = models.CharField(max_length=255, blank=True, null=True)
    registration_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, default='pending')
    
    class Meta:
        indexes = [
            models.Index(fields=['asset_id']),
            models.Index(fields=['serial_number']),
            models.Index(fields=['warranty_end']),
        ]