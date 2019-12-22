from .models import Profile, Location, Tracker

def new_distress(user):
    #Send SMS
    tracker = Tracker.objects.create(user=user)
    url = '/track/{}'.format(tracker.uid)
    