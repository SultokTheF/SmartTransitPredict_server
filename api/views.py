from rest_framework import viewsets
from .models import Vehicle, Route, Stop, Schedule, RealTimeLocation, Prediction, HistoricalData
from .serializers import VehicleSerializer, RouteSerializer, StopSerializer, ScheduleSerializer, RealTimeLocationSerializer, PredictionSerializer, HistoricalDataSerializer

class VehicleViewSet(viewsets.ModelViewSet):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer

class RouteViewSet(viewsets.ModelViewSet):
    queryset = Route.objects.all()
    serializer_class = RouteSerializer

class StopViewSet(viewsets.ModelViewSet):
    queryset = Stop.objects.all()
    serializer_class = StopSerializer

class ScheduleViewSet(viewsets.ModelViewSet):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer

class RealTimeLocationViewSet(viewsets.ModelViewSet):
    queryset = RealTimeLocation.objects.all()
    serializer_class = RealTimeLocationSerializer

class PredictionViewSet(viewsets.ModelViewSet):
    queryset = Prediction.objects.all()
    serializer_class = PredictionSerializer

class HistoricalDataViewSet(viewsets.ModelViewSet):
    queryset = HistoricalData.objects.all()
    serializer_class = HistoricalDataSerializer
