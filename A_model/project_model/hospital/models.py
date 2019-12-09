from django.db import models

# Create your models here.


class Dokter(models.Model):
    nama = models.CharField(max_length=200)
    nomor_telepon = models.CharField(max_length=11)
    bidang = models.CharField(max_length=200)
    jadwal_praktek = models.CharField(max_length=200)
    def __str__(self):
        return self.nama

class Pasien(models.Model):
    nama = models.CharField(max_length=200)
    nomor_telepon = models.CharField(max_length=11)
    alamat = models.CharField(max_length=200)
    keluhan = models.CharField(max_length=200)
    def __str__(self):
        return self.nama
class Resep(models.Model):
    nama = models.CharField(max_length=200)
    total_harga = models.DecimalField(max_digits=25, decimal_places=2)
    kumpulan_obat = models.CharField(max_length=200)
    def __str__(self):
        return self.nama
class Obat(models.Model):
    nama = models.CharField(max_length=200)
    kandungan = models.CharField(max_length=200)
    khasiat = models.CharField(max_length=200)
    def __str__(self):
        return self.nama