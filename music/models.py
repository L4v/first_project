# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Album(models.Model):
    artist = models.CharField(max_length=64)
    album_title = models.CharField(max_length=64)
    genre = models.CharField(max_length=64)
    album_logo = models.CharField(max_length=256)

    def __str__(self):
        return self.album_title + ' - ' + self.artist


class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    file_type = models.CharField(max_length=8)
    song_title = models.CharField(max_length=64)
    is_favorite = models.BooleanField(default=False)

    def __str__(self):
        return self.song_title
