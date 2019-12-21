from .models import Profile, Location

def new_distress(user):
    #Send SMS
    tracker = Tracker(user=user)
    url = '/track/{}'.format(tracker.uid)
    