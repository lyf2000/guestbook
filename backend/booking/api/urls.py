from django.urls import path
from rest_framework import routers

from backend.booking.api.views import PostViewSet, new_review

app_name = 'booking-api'


router = routers.DefaultRouter()
router.register('reviews', PostViewSet, basename='reviews')

urlpatterns = [
    path('new/', new_review, name='rev-creaete'),
] + router.urls
