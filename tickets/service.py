from django.db import transaction
from django.utils import timezone
from .models import Ticket, TicketTier
import uuid


class TicketService:
    @staticmethod
    @transaction.atomic
    def reserve_ticket(user, tier_id: uuid.UUID) -> Ticket:
        # Lock the ticket tier row to prevent race conditions
        tier = TicketTier.objects.select_for_update().get(id=tier_id)

        if tier.quantity_available <= 0:
            raise ValueError('No tickets available for this tier.')

        ticket = Ticket.objects.create(
            tier=tier,
            customer=user,
            status=Ticket.Status.PENDING
        )
        return ticket
