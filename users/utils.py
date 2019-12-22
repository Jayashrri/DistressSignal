from .models import Profile, Location, Tracker, Authorities
from django.conf import settings

from scipy import spatial
from pprint import pprint
import requests
import numpy as np

def nearest_authority(latitude, longitude):
    latset = Authorities.objects.values_list('latitude', flat=True)
    longset = Authorities.objects.values_list('longitude', flat=True)
    nplat = np.array(latset)
    nplat = np.asfarray(nplat,float)
    nplong = np.array(longset)
    nplong = np.asfarray(nplong,float)
    result = np.dstack([nplong.ravel(),nplat.ravel()])[0]
    tree = spatial.cKDTree(result)
    point = [latitude, longitude]
    distance, nearest = tree.query(point)
    index = nearest
    return index

def send_message(SID, EKEY, ETOKEN, sms_from, sms_to, sms_body):
    return requests.post('https://twilix.exotel.in/v1/Accounts/{sid}/Sms/send.json'.format(sid=SID),
        auth=(EKEY, ETOKEN),
        data={
            'From': sms_from,
            'To': sms_to,
            'Body': sms_body
        })

def new_distress(user, index):
    tracker = Tracker.objects.create(user=user)
    url = 'hello.com/track/{}'.format(tracker.uid)
    r = send_message(settings.SID, settings.EKEY, settings.ETOKEN,
        sms_from='9945235123',
        sms_to='9566343697',
        sms_body='This is a test message being sent using Exotel with a (%s) and (%d). If this is being abused, report to 08088919888' % (url,1))
    print(r.status_code)
    pprint(r.json())