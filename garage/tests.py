from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from .models import Car, Track, LapTime, Tag
import datetime


class CarModelTest(TestCase):
    """Tests for Car model"""

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='test1234')
        self.car = Car.objects.create(
            owner=self.user,
            brand='BMW',
            model='M3',
            year=2023,
            horsepower=510,
            fuel_type='petrol'
        )

    def test_car_str(self):
        self.assertEqual(str(self.car), '2023 BMW M3')

    def test_car_owner(self):
        self.assertEqual(self.car.owner, self.user)

    def test_car_fuel_type(self):
        self.assertEqual(self.car.fuel_type, 'petrol')


class TrackModelTest(TestCase):
    """Tests for Track model"""

    def setUp(self):
        self.track = Track.objects.create(
            name='Monza',
            location='Italy',
            length_km=5.79
        )

    def test_track_str(self):
        self.assertEqual(str(self.track), 'Monza (Italy)')

    def test_track_length(self):
        self.assertEqual(float(self.track.length_km), 5.79)


class LapTimeModelTest(TestCase):
    """Tests for LapTime model"""

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='test1234')
        self.car = Car.objects.create(
            owner=self.user, brand='Ferrari', model='488',
            year=2022, fuel_type='petrol'
        )
        self.track = Track.objects.create(
            name='Spa', location='Belgium', length_km=7.00
        )
        self.lap = LapTime.objects.create(
            car=self.car, track=self.track,
            minutes=2, seconds=18, milliseconds=500,
            date=datetime.date.today()
        )

    def test_lap_total_milliseconds(self):
        self.assertEqual(self.lap.total_milliseconds(), 138500)

    def test_lap_str(self):
        self.assertIn('2:18', str(self.lap))


class CarViewTest(TestCase):
    """Tests for Car views"""

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='test1234')
        self.car = Car.objects.create(
            owner=self.user, brand='Porsche', model='911',
            year=2023, fuel_type='petrol'
        )

    def test_car_list_requires_login(self):
        response = self.client.get(reverse('car_list'))
        self.assertEqual(response.status_code, 302)

    def test_car_list_logged_in(self):
        self.client.login(username='testuser', password='test1234')
        response = self.client.get(reverse('car_list'))
        self.assertEqual(response.status_code, 200)

    def test_car_detail(self):
        self.client.login(username='testuser', password='test1234')
        response = self.client.get(reverse('car_detail', args=[self.car.pk]))
        self.assertEqual(response.status_code, 200)

    def test_car_create(self):
        self.client.login(username='testuser', password='test1234')
        response = self.client.post(reverse('car_create'), {
            'brand': 'Audi',
            'model': 'R8',
            'year': 2023,
            'horsepower': 620,
            'fuel_type': 'petrol'
        })
        self.assertEqual(Car.objects.filter(brand='Audi').count(), 1)

    def test_car_delete(self):
        self.client.login(username='testuser', password='test1234')
        response = self.client.post(reverse('car_delete', args=[self.car.pk]))
        self.assertEqual(Car.objects.filter(pk=self.car.pk).count(), 0)

    def test_other_user_cannot_see_car(self):
        other_user = User.objects.create_user(username='other', password='test1234')
        self.client.login(username='other', password='test1234')
        response = self.client.get(reverse('car_detail', args=[self.car.pk]))
        self.assertEqual(response.status_code, 404)
