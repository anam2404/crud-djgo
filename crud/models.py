from django.db import models

# Create your models here.
class Pegawaiudb(models.Model):
    sid = models.CharField(max_length=4)
    snama = models.CharField(max_length=255)
    snip = models.CharField(max_length=255)
    sdivisi = models.CharField(max_length=255)
    salamat = models.CharField(max_length=255)
    sjenkel = models.CharField(max_length=255)

    def __str__(self):
        return self.snamapegawai