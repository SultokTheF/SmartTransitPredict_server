from django.db import models

class Vehicle(models.Model):
    vehicle_id = models.AutoField(primary_key=True)
    type = models.CharField(max_length=50)
    capacity = models.IntegerField()
    model = models.CharField(max_length=100)
    status = models.CharField(max_length=50)  # Active, Inactive, Maintenance, etc.
    operator = models.CharField(max_length=100)

class Route(models.Model):
    route_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    start_point_longitude = models.FloatField()
    start_point_latitude = models.FloatField()
    end_point_longitude = models.FloatField()
    end_point_latitude = models.FloatField()
    distance = models.FloatField()  # Distance in km
    average_travel_time = models.DurationField()

class Stop(models.Model):
    stop_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    longitude = models.FloatField()
    latitude = models.FloatField()
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
    longitude = models.FloatField()
    latitude = models.FloatField()
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
