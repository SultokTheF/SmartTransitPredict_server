from django.db import models

class Vehicle(models.Model):
    vehicle_id = models.CharField(max_length=50, primary_key=True)
    type = models.CharField(max_length=50)
    capacity = models.IntegerField()
    operator = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    status = models.CharField(max_length=50)  # Active, Inactive, Maintenance, etc.

class Route(models.Model):
    route_id = models.CharField(max_length=50, primary_key=True)
    name = models.CharField(max_length=100)
    start_point = models.CharField(max_length=100)
    end_point = models.CharField(max_length=100)
    distance = models.FloatField()  # Distance in km
    average_travel_time = models.DurationField()

class Stop(models.Model):
    stop_id = models.CharField(max_length=50, primary_key=True)
    name = models.CharField(max_length=100)
    location_coordinates = models.CharField(max_length=100)
    zone = models.CharField(max_length=50)

class Schedule(models.Model):
    schedule_id = models.AutoField(primary_key=True)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    route = models.ForeignKey(Route, on_delete=models.CASCADE)
    departure_time = models.DateTimeField()
    arrival_time = models.DateTimeField()
    day_of_week = models.CharField(max_length=10)
    status = models.CharField(max_length=50)

class RealTimeLocation(models.Model):
    record_id = models.AutoField(primary_key=True)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    route = models.ForeignKey(Route, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    latitude = models.FloatField()
    longitude = models.FloatField()
    speed = models.FloatField()  # Speed in km/h

class Prediction(models.Model):
    prediction_id = models.AutoField(primary_key=True)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    stop = models.ForeignKey(Stop, on_delete=models.CASCADE)
    predicted_arrival_time = models.DateTimeField()
    confidence_score = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)

class HistoricalData(models.Model):
    history_id = models.AutoField(primary_key=True)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    route = models.ForeignKey(Route, on_delete=models.CASCADE)
    stop = models.ForeignKey(Stop, on_delete=models.CASCADE)
    actual_arrival_time = models.DateTimeField()
    timestamp = models.DateTimeField()
