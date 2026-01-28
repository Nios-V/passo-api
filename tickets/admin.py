from django.contrib import admin
from .models import Event, TicketTier, Ticket

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'location', 'capacity', 'created_at', 'updated_at')
    search_fields = ('title', 'location')
    list_filter = ('date',)


@admin.register(TicketTier)
class TicketTierAdmin(admin.ModelAdmin):
    list_display = ('name', 'event', 'price', 'quantity_available')
    search_fields = ('name', 'event__title')
    list_filter = ('event',)


@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ('id', 'tier', 'status', 'purchased_at', 'created_at')
    search_fields = ('tier__name',)
    list_filter = ('status',)