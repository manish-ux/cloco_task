from django.db import models
from core.models import TimeStampModel


class GenderChoice(models.TextChoices):
    male = "m", "m"
    female = "f", "f"
    others = "o", "o"


class MusicGenreChoice(models.TextChoices):
    rnb = "rnb", "rnb"
    country = "country", "country"
    classic = "classic", "classic"
    rock = "rock", "rock"
    jazz = "jazz", "jazz"


# Create your models here.
class User(TimeStampModel):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    password = models.CharField(max_length=500)
    phone = models.CharField(max_length=20)
    dob = models.DateTimeField()
    gender = models.CharField(choices=GenderChoice.choices,max_length=15)
    address = models.CharField(max_length=255)


class Artist(TimeStampModel):
    name = models.CharField(max_length=255)
    dob = models.DateTimeField()
    gender = models.CharField(choices=GenderChoice.choices,max_length=15)
    address = models.CharField(max_length=255)
    first_release_year = models.IntegerField()
    no_of_albums_released = models.IntegerField()


class Music(TimeStampModel):
    artist_id = models.ForeignKey('Artist',on_delete=models.SET_NULL,related_name = "artist_music_album",null=True)
    title = models.CharField(max_length=255)
    album_name = models.CharField(max_length=255)
    genre = models.CharField(choices=MusicGenreChoice.choices,max_length=15)