import uuid
from django.db import models

class Event(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateTimeField()
    location = models.CharField(max_length=200)
    capacity = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
class TicketTier(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    event = models.ForeignKey(Event, related_name='ticket_tiers', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    quantity_available = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.name} - {self.event.title}"

class Ticket(models.Model):
    class Status(models.TextChoices):
        AVAILABLE = 'available', 'Available'
        PENDING = 'pending', 'Pending'
        SOLD = 'sold', 'Sold'
        CANCELLED = 'cancelled', 'Cancelled'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    tier = models.ForeignKey(TicketTier, related_name='tickets', on_delete=models.CASCADE)
    # customer = models.ForeignKey(Customer, related_name='customer', on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=Status.choices, default=Status.AVAILABLE)
    purchased_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Ticket {self.id} ({self.tier.name}) - {self.status}"
    