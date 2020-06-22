from rest_framework import serializers

from backend.booking.models import Review


class ReviewSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format="%a, %b %Y", required=False)

    class Meta:
        model = Review
        fields = ('id', 'author_name', 'text', 'created_at')


    # def create(self, validated_data):
    #     user = self.context['request'].user
    #     return Post.objects.create(
    #         **validated_data,
    #         author=user
    #     )
