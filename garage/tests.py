from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Car, Track, LapTime, Tag
from datetime import date

class GarageModelTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password123')
        self.tag = Tag.objects.create(name='Classic')
        self.track = Track.objects.create(name='Istanbul Park', location='Istanbul', length_km=5.33)
        self.car = Car.objects.create(
            owner=self.user,
            brand='Porsche',
            model='911',
            year=2020,
            fuel_type='petrol'
        )
        self.car.tags.add(self.tag)

    def test_car_creation(self):
        """Test if a Car is created successfully and string representation is correct."""
        self.assertEqual(str(self.car), '2020 Porsche 911')
        self.assertEqual(self.car.tags.count(), 1)
        self.assertEqual(self.car.owner.username, 'testuser')

    def test_track_string_representation(self):
        """Test track string representation."""
        self.assertEqual(str(self.track), 'Istanbul Park (Istanbul)')

    def test_laptime_creation_and_calculation(self):
        """Test LapTime creation and total_milliseconds method."""
        lap = LapTime.objects.create(
            car=self.car,
            track=self.track,
            minutes=1,
            seconds=55,
            milliseconds=250,
            date=date.today()
        )
        # 1 min = 60000ms, 55 sec = 55000ms, 250ms -> Total = 115250
        self.assertEqual(lap.total_milliseconds(), 115250)
        self.assertTrue('Porsche 911' in str(lap))

class GarageViewTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='password123')
        self.car = Car.objects.create(
            owner=self.user,
            brand='Honda',
            model='Civic',
            year=2015
        )

    def test_home_view_redirects_unauthenticated(self):
        """Test that unauthenticated users are redirected to login."""
        response = self.client.get(reverse('home'))
        self.assertNotEqual(response.status_code, 200)
        self.assertTrue(response.url.startswith('/accounts/login/'))

    def test_home_view_authenticated(self):
        """Test that authenticated users can access the home dashboard."""
        self.client.login(username='testuser', password='password123')
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'garage/home.html')

    def test_car_list_view(self):
        """Test the car list view displays user cars."""
        self.client.login(username='testuser', password='password123')
        response = self.client.get(reverse('car_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Honda')

    def test_car_create_view(self):
        """Test creating a car via POST request."""
        self.client.login(username='testuser', password='password123')
        response = self.client.post(reverse('car_create'), {
            'brand': 'Toyota',
            'model': 'Corolla',
            'year': 2022,
            'fuel_type': 'petrol'
        })
        # Should redirect to car_detail after creation
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Car.objects.filter(brand='Toyota').count(), 1)

class GarageAPITests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='apiuser', password='password123')
        self.car = Car.objects.create(owner=self.user, brand='Mazda', model='RX-7', year=1995)

    def test_api_car_list_unauthenticated(self):
        response = self.client.get(reverse('api_cars'))
        self.assertEqual(response.status_code, 403) # Forbidden

    def test_api_car_list_authenticated(self):
        self.client.login(username='apiuser', password='password123')
        response = self.client.get(reverse('api_cars'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 1)
        self.assertEqual(response.json()[0]['brand'], 'Mazda')
