from django.contrib import admin
from .models import Car, Track, LapTime, Tag


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ['brand', 'model', 'year', 'owner', 'fuel_type']
    search_fields = ['brand', 'model', 'owner__username']
    list_filter = []
    actions = ['delete_selected_cars']

    def delete_selected_cars(self, request, queryset):
        count = queryset.count()
        queryset.delete()
        self.message_user(request, f"{count} araç başarıyla silindi.")
    delete_selected_cars.short_description = "Seçili araçları sil"


@admin.register(Track)
class TrackAdmin(admin.ModelAdmin):
    list_display = ['name', 'location', 'length_km']
    search_fields = ['name', 'location']
    list_filter = []
    actions = ['delete_selected_tracks']

    def delete_selected_tracks(self, request, queryset):
        count = queryset.count()
        queryset.delete()
        self.message_user(request, f"{count} pist başarıyla silindi.")
    delete_selected_tracks.short_description = "Seçili pistleri sil"


@admin.register(LapTime)
class LapTimeAdmin(admin.ModelAdmin):
    list_display = ['car', 'track', 'minutes', 'seconds', 'milliseconds', 'date', 'notes']
    search_fields = ['car__brand', 'car__model', 'track__name']
    list_filter = []
    actions = ['delete_selected_laptimes']

    def delete_selected_laptimes(self, request, queryset):
        count = queryset.count()
        queryset.delete()
        self.message_user(request, f"{count} tur zamanı başarıyla silindi.")
    delete_selected_laptimes.short_description = "Seçili tur zamanlarını sil"


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name']