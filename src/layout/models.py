from django.db import models


class News(models.Model):
    title = models.CharField(max_length=50)
    text = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    image = models.ImageField(blank=True, upload_to="news/")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "News"


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
    image = models.ImageField(blank=True, upload_to="profile/")
    interests = models.ManyToManyField(blank=True, to=Interest)

    def __str__(self):
        return self.name


class Event(models.Model):
    title = models.CharField(max_length=50)
    start_at = models.DateTimeField()
    end_at = models.DateTimeField()
    text = models.TextField()

    image = models.ImageField(blank=True, upload_to="events/")
    interests = models.ManyToManyField(blank=True, to=Interest)

    def __str__(self):
        return self.title
