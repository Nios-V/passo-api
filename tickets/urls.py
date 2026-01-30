from django.urls import path
from .views import EventRetrieveUpdateDestroyView, EventListCreateView, TicketReservationView

urlpatterns = [
    path('events/', EventListCreateView.as_view(), name='event-list-create'),
    path('events/<uuid:pk>/', EventRetrieveUpdateDestroyView.as_view(),
         name='event-detail'),
    path('tickets/reserve/', TicketReservationView.as_view(), name='ticket-reserve'),
]
