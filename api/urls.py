from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'vehicles', views.VehicleViewSet)
router.register(r'routes', views.RouteViewSet)
router.register(r'stops', views.StopViewSet)
router.register(r'schedules', views.ScheduleViewSet)
router.register(r'realtime_locations', views.RealTimeLocationViewSet)
router.register(r'predictions', views.PredictionViewSet)
router.register(r'historical_data', views.HistoricalDataViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
