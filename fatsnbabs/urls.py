from django.contrib import admin
from django.urls import path, include
from booking_system import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index_view, name='index'),
    path('menus', views.menu_view, name='menus'),
]