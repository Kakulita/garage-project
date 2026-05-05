from rest_framework import generics, permissions
from .models import Car, LapTime, Track
from .serializers import CarSerializer, LapTimeSerializer, TrackSerializer


class CarListCreateAPI(generics.ListCreateAPIView):
    """GET all cars / POST new car"""
    serializer_class = CarSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Car.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class CarDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    """GET / PUT / DELETE a single car"""
    serializer_class = CarSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Car.objects.filter(owner=self.request.user)


class LapTimeListCreateAPI(generics.ListCreateAPIView):
    """GET all lap times / POST new lap time"""
    serializer_class = LapTimeSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return LapTime.objects.filter(car__owner=self.request.user)


class TrackListCreateAPI(generics.ListCreateAPIView):
    """GET all tracks / POST new track"""
    serializer_class = TrackSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Track.objects.all()
