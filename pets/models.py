from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

class Mascota(models.Model):
    namepet = models.CharField(max_length=6)
    datenac = models.DateField()
    edad = models.IntegerField()
    nameraza = models.CharField(max_length=15)
    photo = models.ImageField(upload_to='mascotas', blank=True, null=True)
    amo = models.ForeignKey(User)

def __unicode__(self,):
     return str(self.photo)

class Message(models.Model):
    remitente = models.CharField(max_length=15)
    destinatario = models.CharField(max_length=15)
    asunto = models.CharField(max_length=10)
    mensaje = models.TextField()

