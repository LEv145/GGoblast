from django.db import models


class Interest(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Profile(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

    telephone_number = models.CharField(blank=True, max_length=20)
    email = models.CharField(blank=True, max_length=50)
    # image = models.ImageField(blank=True, upload_to="profile/")

    interests = models.ManyToManyField(blank=True, to=Interest)

    def __str__(self):
        return self.name


class Event(models.Model):
    name = models.CharField(max_length=50)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    description = models.TextField()

    # image = models.ImageField(blank=True, upload_to="events/")
    interests = models.ManyToManyField(blank=True, to=Interest)

    def __str__(self):
        return self.name


