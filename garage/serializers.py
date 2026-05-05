from rest_framework import serializers
from .models import Car, LapTime, Track, Tag


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name']


class TrackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Track
        fields = ['id', 'name', 'location', 'length_km']


class LapTimeSerializer(serializers.ModelSerializer):
    track = TrackSerializer(read_only=True)
    track_id = serializers.PrimaryKeyRelatedField(
        queryset=Track.objects.all(), source='track', write_only=True
    )

    class Meta:
        model = LapTime
        fields = ['id', 'track', 'track_id', 'minutes', 'seconds', 'milliseconds', 'date', 'notes']


class CarSerializer(serializers.ModelSerializer):
    lap_times = LapTimeSerializer(many=True, read_only=True)
    tags = TagSerializer(many=True, read_only=True)
    owner = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Car
        fields = ['id', 'owner', 'brand', 'model', 'year', 'horsepower', 'fuel_type', 'tags', 'lap_times']
