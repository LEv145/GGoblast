from django.contrib import admin

from .models import EventInterest, ProfileInterest, Profile, Event


admin.site.register(EventInterest)
admin.site.register(ProfileInterest)
admin.site.register(Profile)
admin.site.register(Event)
