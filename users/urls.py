from django.urls import path
from . import views

urlpatterns = [
    path('distress', views.distress_signal, name='distress'),
    path('tracker/<slug:uid>', views.location_history, name='tracker'),
]
