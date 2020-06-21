from django.urls import path

from backend.booking.views import index

app_name = 'booking'

urlpatterns = [
    path('', index, name='index'),
]
