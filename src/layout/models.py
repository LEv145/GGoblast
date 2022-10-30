from django.db import models


class Profile(models.Model):
    name = models.TextField()
    surname = models.TextField()
    password = models.TextField()

    telephone_number = models.TextField(blank=True)
    email = models.TextField(blank=True)
    image = models.ImageField(blank=True, upload_to="profile/")

    def __str__(self) -> str:
        return self.name


class ProfileInterest(models.Model):
    name = models.TextField()
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name


class Event(models.Model):
    name = models.TextField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    description = models.TextField()

    image = models.ImageField(blank=True, upload_to="events/")

    def __str__(self) -> str:
        return self.name


class EventInterest(models.Model):
    name = models.TextField()
    event = models.ForeignKey(Event, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name