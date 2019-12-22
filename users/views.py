from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication, TokenAuthentication

from .models import Profile, Location, Tracker
from .utils import new_distress, nearest_authority

# Create your views here.

def location_history(request, uid):
    if request.method == 'GET':
        tracker = Tracker.objects.get(uid=uid)
        user = tracker.user
        history = Location.objects.filter(user=user)
        return render(request, 'tracker.html', {'locationdata': history, 
                                                'name': user.name, 
                                                'phone': user.phone })

@api_view(['POST'])
@authentication_classes([SessionAuthentication,TokenAuthentication])
@permission_classes([IsAuthenticated])
def distress_signal(request):
    profile = request.user
    #location = request.GET.get('location')
    latitude = request.data['latitude']
    longitude = request.data['longitude']
    if profile.distress ==  False:
        profile.distress = True
        profile.save()
        index = nearest_authority(latitude, longitude)
        new_distress(profile, index)
    #print("Latitude: ", latitude, ", Longitude: ", longitude)
    newLocation = Location(user=profile, latitude=latitude, longitude=longitude)
    newLocation.save()
    return Response({})
