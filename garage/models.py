from django.db import models
from django.contrib.auth.models import User


class Tag(models.Model):
    """Araç etiketi: Klasik, Modifiye, Track Car vb."""
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Track(models.Model):
    """Pist bilgisi"""
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    length_km = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"{self.name} ({self.location})"


class Car(models.Model):
    """Kullanıcının garajındaki araç"""
    FUEL_CHOICES = [
        ('petrol', 'Benzin'),
        ('diesel', 'Dizel'),
        ('electric', 'Elektrik'),
        ('hybrid', 'Hibrit'),
    ]

    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='cars')
    brand = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    year = models.PositiveIntegerField()
    horsepower = models.PositiveIntegerField(null=True, blank=True)
    fuel_type = models.CharField(max_length=10, choices=FUEL_CHOICES, default='petrol')
    image = models.ImageField(upload_to='cars/', null=True, blank=True)
    tags = models.ManyToManyField(Tag, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.year} {self.brand} {self.model}"


class LapTime(models.Model):
    """Tur süresi kaydı"""
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='lap_times')
    track = models.ForeignKey(Track, on_delete=models.CASCADE, related_name='lap_times')
    minutes = models.PositiveIntegerField()
    seconds = models.PositiveIntegerField()
    milliseconds = models.PositiveIntegerField()
    date = models.DateField()
    notes = models.TextField(blank=True)

    class Meta:
        ordering = ['minutes', 'seconds', 'milliseconds']

    def total_milliseconds(self):
        """Karşılaştırma için toplam ms"""
        return (self.minutes * 60000) + (self.seconds * 1000) + self.milliseconds

    def __str__(self):
        return f"{self.car} – {self.minutes}:{self.seconds:02d}.{self.milliseconds:03d}"