from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django_filters.rest_framework import DjangoFilterBackend
from .service import TicketService
from tickets.filters import EventFilter
from .models import Event
from .serializer import EventSerializer, ReservationRequestSerializer, TicketSerializer
from .permissions import IsOrganizer, IsOwnerOrReadOnly


class EventListView(generics.ListAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = EventFilter


class EventCreateView(generics.CreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [IsOrganizer]


class EventRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [IsOwnerOrReadOnly]


class TicketReservationView(APIView):
    def post(self, request):
        serializer = ReservationRequestSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        try:
            ticket = TicketService.reserve_ticket(
                user=request.user,
                tier_id=serializer.validated_data['tier_id']
            )

            output_serializer = TicketSerializer(ticket)
            return Response(output_serializer.data, status=status.HTTP_201_CREATED)
        except ValueError as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
