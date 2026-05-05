from django.contrib import admin
from .models import Car, Track, LapTime, Tag


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ['brand', 'model', 'year', 'owner', 'fuel_type']
    search_fields = ['brand', 'model', 'owner__username']
    list_filter = ['fuel_type', 'year']


@admin.register(Track)
class TrackAdmin(admin.ModelAdmin):
    list_display = ['name', 'location', 'length_km']


@admin.register(LapTime)
class LapTimeAdmin(admin.ModelAdmin):
    list_display = ['car', 'track', 'minutes', 'seconds', 'milliseconds', 'date']


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name']
