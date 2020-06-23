from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response

from backend.booking.api.serializers import ReviewSerializer
from backend.booking.models import Review
from rest_framework.permissions import AllowAny


class PostViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [AllowAny]
    # ordering = ('created_at', )


@api_view(['POST'])
def new_review(request):
    a = 42
    r = ReviewSerializer(data=request.data)
    if r.is_valid():
        a = 44
    # user = request.user
    # user.bookmark_post(pk)
    return Response(status=200)