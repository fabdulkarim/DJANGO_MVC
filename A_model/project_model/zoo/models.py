from django.db import models

# Create your models here.


class Hewan(models.Model):
    nama = models.CharField(max_length=200)
    species = models.CharField(max_length=200)
    berat = models.DecimalField(max_digits=8, decimal_places=2)
    umur = models.CharField(max_length=200)
    def __str__(self):
        return self.nama
class Kandang(models.Model):
    nama = models.CharField(max_length=200)
    isi_kandang = models.CharField(max_length=200)
    luas_kandang = models.DecimalField(max_digits=25, decimal_places=2)
    def __str__(self):
        return self.nama
class Penjaga(models.Model):
    nama = models.CharField(max_length=200)
    nomor_telepon = models.CharField(max_length=11)
    jadwal_jaga = models.CharField(max_length=200)
    def __str__(self):
        return self.nama
class Pengunjung(models.Model):
    nama = models.CharField(max_length=200)
    nomor_telepon = models.CharField(max_length=11)
    hari_berkunjung = models.DateField('Hari Berkunjung')
    def __str__(self):
        return self.nama