from django.contrib import admin
from django.urls import path, include
from booking_system import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index_view, name='index'),
    path('menus', views.menu_view, name='menus'),
    path('booking', views.add_reservation, name='booking'),
    path('mybookings', views.mybookings_view, name='mybookings'),
    path('edit_booking/<reservation_id>', views.edit_booking, name='edit_booking'),
    path('delete_booking/<reservation_id>', views.delete_booking, name='delete_booking'),
    path('location', views.location_view, name='location'),
    path('accounts/', include('allauth.urls')),
]