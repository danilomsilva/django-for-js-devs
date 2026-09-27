from rest_framework import serializers

from .models import Greeting


class GreetingSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(slug_field="name", read_only=True, allow_null=True)

    class Meta:
        model = Greeting
        fields = ["id", "message", "category", "created_at"]
