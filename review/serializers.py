from rest_framework import serializers

from .models import Review


class ReviewSerializer(serializers.ModelSerializer):
    """Serializer for Review obj"""
    reviewer = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = Review
        fields = ('id', 'rating', 'title', 'company', 'reviewer', 'summary')
        read_only_fields = ('id',)
