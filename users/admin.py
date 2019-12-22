from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from django.shortcuts import HttpResponseRedirect

from .models import Profile, Location, Tracker
from .forms import ProfileChangeForm, ProfileCreationForm

# Register your models here.
class ProfileAdmin(UserAdmin):
    add_form = ProfileCreationForm
    form = ProfileChangeForm
    model = Profile
    list_display = ('email', 'username', 'phone')
    list_filter = ('email', 'is_staff', 'is_active')

admin.site.register(Profile)
admin.site.register(Location)
admin.site.register(Tracker)