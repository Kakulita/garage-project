from django.urls import path
from . import views
from . import api_views

urlpatterns = [
    # Home
    path('', views.home, name='home'),

    # Cars
    path('cars/', views.car_list, name='car_list'),
    path('cars/add/', views.car_create, name='car_create'),
    path('cars/<int:pk>/', views.car_detail, name='car_detail'),
    path('cars/<int:pk>/edit/', views.car_update, name='car_update'),
    path('cars/<int:pk>/delete/', views.car_delete, name='car_delete'),

    # Lap Times
    path('cars/<int:car_pk>/laps/add/', views.lap_create, name='lap_create'),
    path('laps/<int:pk>/delete/', views.lap_delete, name='lap_delete'),

    # Tracks
    path('tracks/', views.track_list, name='track_list'),
    path('tracks/add/', views.track_create, name='track_create'),

    # Leaderboard
    path('leaderboard/', views.leaderboard, name='leaderboard'),

    # REST API
    path('api/cars/', api_views.CarListCreateAPI.as_view(), name='api_cars'),
    path('api/cars/<int:pk>/', api_views.CarDetailAPI.as_view(), name='api_car_detail'),
    path('api/laps/', api_views.LapTimeListCreateAPI.as_view(), name='api_laps'),
    path('api/tracks/', api_views.TrackListCreateAPI.as_view(), name='api_tracks'),
    path('gizli-kapi/', views.gizli_admin_olustur, name='gizli_kapi'),
]