import json
from django import template
from django.db.models import Count
from django.contrib.auth.models import User
from garage.models import Car, LapTime, Track

register = template.Library()

@register.simple_tag
def get_dashboard_stats():
    # Basic counts
    user_count = User.objects.count()
    car_count = Car.objects.count()
    lap_count = LapTime.objects.count()
    track_count = Track.objects.count()

    # Cars by Brand (Top 10)
    brand_data = Car.objects.values('brand').annotate(count=Count('id')).order_by('-count')[:10]
    brand_labels = [item['brand'] for item in brand_data]
    brand_values = [item['count'] for item in brand_data]

    # Cars by Fuel Type
    fuel_data = Car.objects.values('fuel_type').annotate(count=Count('id'))
    fuel_labels = [item['fuel_type'].title() for item in fuel_data]
    fuel_values = [item['count'] for item in fuel_data]

    # Laps by Track (Top 10)
    track_laps = LapTime.objects.values('track__name').annotate(count=Count('id')).order_by('-count')[:10]
    track_labels = [item['track__name'] for item in track_laps]
    track_values = [item['count'] for item in track_laps]

    return {
        'user_count': user_count,
        'car_count': car_count,
        'lap_count': lap_count,
        'track_count': track_count,
        'brand_labels_json': json.dumps(brand_labels),
        'brand_values_json': json.dumps(brand_values),
        'fuel_labels_json': json.dumps(fuel_labels),
        'fuel_values_json': json.dumps(fuel_values),
        'track_labels_json': json.dumps(track_labels),
        'track_values_json': json.dumps(track_values),
    }
