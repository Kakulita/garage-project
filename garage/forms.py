from django import forms
from .models import Car, LapTime, Track, Tag


class CarForm(forms.ModelForm):
    """Form for adding/editing a car"""
    class Meta:
        model = Car
        fields = ['brand', 'model', 'year', 'horsepower', 'fuel_type', 'image', 'tags']
        widgets = {
            'tags': forms.CheckboxSelectMultiple(),
        }


class LapTimeForm(forms.ModelForm):
    """Form for adding a lap time"""
    class Meta:
        model = LapTime
        fields = ['track', 'minutes', 'seconds', 'milliseconds', 'date', 'notes']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'notes': forms.Textarea(attrs={'rows': 3}),
        }


class TrackForm(forms.ModelForm):
    """Form for adding a track"""
    class Meta:
        model = Track
        fields = ['name', 'location', 'length_km']