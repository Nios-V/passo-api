from rest_framework import serializers
from .models import Event, Ticket, TicketTier


class TicketTierSerializer(serializers.ModelSerializer):
    class Meta:
        model = TicketTier
        fields = ['id', 'name', 'price', 'quantity_available']


class EventSerializer(serializers.ModelSerializer):
    ticket_tiers = TicketTierSerializer(many=True, read_only=True)

    class Meta:
        model = Event
        fields = ['id', 'title', 'description', 'date',
                  'location', 'capacity', 'ticket_tiers']


class TicketSerializer(serializers.ModelSerializer):
    tier = TicketTierSerializer(read_only=True)

    class Meta:
        model = Ticket
        fields = ['id', 'tier', 'customer', 'status', 'reserved_at']


class ReservationRequestSerializer(serializers.Serializer):
    tier_id = serializers.UUIDField()
