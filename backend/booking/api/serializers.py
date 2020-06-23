from rest_framework import serializers

from backend.booking.models import Review


class ReviewSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format="%a, %b %Y", required=False)
    image = serializers.ImageField(required=False)

    class Meta:
        model = Review
        fields = ('id', 'author_name', 'text', 'created_at', 'image',)

    def validate_author_name(self, value):
        """
        Check that the blog post is about Django.
        """
        if len(value) < 3 or len(value) > 32:
            raise serializers.ValidationError("[3; 32]")
        return value

    def validate_text(self, value):
        """
        Check that the blog post is about Django.
        """
        if len(value) < 16 or len(value) > 512:
            raise serializers.ValidationError("[16; 512]")
        return value

    # def create(self, validated_data):
    #     user = self.context['request'].user
    #     return Post.objects.create(
    #         **validated_data,
    #         author=user
    #     )
