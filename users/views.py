from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .models import Profile, Location
from .utils import new_distress

# Create your views here.

def location_history(request, uid):
    if request.method == 'GET':
        user = Tracker.objects.get(uid=uid)
        profile = Profile.objects.get(user=user)
        history = Location.objects.get(user=user)
        return render(request, 'tracker.html', {'locationdata': history, 
                                                'name': user.name, 
                                                'phone': profile.phone })

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def distress_signal(request):
    user = request.user
    profile = Profile.objects.get(user=user)
    if profile.distress ==  False:
        profile.distress = True
        new_distress(user)
    location = request.GET.get('location')
    latitude = location['latitude']
    longitude = location['longitude']
    newLocation = Location(user=user, latitude=latitude, longitude=longitude)
    newLocation.save()
    return Response({})
