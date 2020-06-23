from rest_framework import viewsets
from backend.booking.api.serializers import ReviewSerializer
from backend.booking.models import Review
from rest_framework.permissions import AllowAny


class PostViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [AllowAny]
    # ordering = ('created_at', )
