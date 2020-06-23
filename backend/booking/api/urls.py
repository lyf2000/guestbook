from django.urls import path
from rest_framework import routers

from backend.booking.api.views import PostViewSet

app_name = 'booking-api'


router = routers.DefaultRouter()
router.register('reviews', PostViewSet, basename='reviews')

urlpatterns = [
    # path('bookmark/<int:pk>', bookmark_post, name='bookmark'),
] + router.urls
