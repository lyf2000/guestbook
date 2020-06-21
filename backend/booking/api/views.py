from rest_framework import viewsets
from backend.booking.api.serializers import ReviewSerializer
from backend.booking.models import Review
from rest_framework.permissions import AllowAny


class PostViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    # pagination_class = MyPaginator
    # filter_backends = (SearchFilter, OrderingFilter, PostTagFilter)
    permission_classes = [AllowAny]
    # ordering = ('-created',)
