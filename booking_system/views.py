from django.shortcuts import render, redirect, HttpResponse, get_list_or_404, \
    get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Reservation
from django.contrib import messages
from datetime import date


# Create your views here.
def index_view(request):
    return render(request, 'index.html')

@login_required
def add_reservation(request):

    if request.method == 'POST':
        form = ReservationForm(request.POST)

        if form.is_valid():
            reserv = form.save(commit=False)
            reserv.client = request.user
            reserv.save()
            messages.success(
                request, 'Your reservation request has been submitted succesfully.'
                )
        else:
            messages.error(request, 'Sorry, that table has already been booked.')
            reserv = form.instance.date

    form = ReservationForm()
    context = {
        'form': form,
    }
    return render(request, 'table_booking.html', context)

@login_required
def manage_bookings(request):
    try:
        reservations = get_list_or_404(Reservation, client=request.user)
    except Exception:
        reservations = None

    form = ReservationForm()
    context = {
        'reservations': reservations,
    }
    return render(request, 'manage_bookings.html', context)

@login_required
def edit_booking(request, reservation_id):


    reservation = get_object_or_404(Reservation, id=reservation_id)
    if request.method == 'POST':
        form = ReservationForm(request.POST, instance=reservation)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thank you, your reservation has been updated succesfully.')
            return redirect('manage_bookings')
        else:
            messages.error(request, 'Sorry, that table has already been booked.')

    form = ReservationForm(instance=reservation)
    context = {
        'form': form,
    }
    return render(request, 'edit_booking.html', context)

@login_required
def delete_booking(request, reservation_id):
    reservation = get_object_or_404(Reservation, id=reservation_id)
    reservation.delete()
    messages.success(request, 'Your reservation has been deleted successfully.')
    return redirect('mybookings')