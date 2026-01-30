from django.urls import path
from .views import EventRetrieveUpdateDestroyView, EventCreateView, EventListView, TicketReservationView

urlpatterns = [
    path('events/', EventListView.as_view(), name='event-list'),
    path('events/', EventCreateView.as_view(), name='event-create'),
    path('events/<uuid:pk>/', EventRetrieveUpdateDestroyView.as_view(),
         name='event-detail'),
    path('tickets/reserve/', TicketReservationView.as_view(), name='ticket-reserve'),
]
