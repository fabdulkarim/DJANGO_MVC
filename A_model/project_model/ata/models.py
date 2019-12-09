from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class Direksi(models.Model):
    nama_lengkap = models.CharField(max_length=200)
    nomor_telepon = models.CharField(max_length=11)
    jabatan = models.CharField(max_length=200)

    def __str__(self):
        return self.nama_lengkap
class Mentee(models.Model):
    nama = models.CharField(max_length=200)
    nomor_telepon = models.CharField(max_length=11)
    nomor_absen = models.IntegerField(validators=[MaxValueValidator(100),MinValueValidator(1)])
    nilai_rata_rata = models.DecimalField(max_digits=5, decimal_places=2, validators=[MaxValueValidator(100),MinValueValidator(0)])
    def __str__(self):
        return self.nama
class MataPelajaran(models.Model):
    nama_pelajaran = models.CharField(max_length=200)
    jadwal_dimulai = models.DateTimeField('Jadwal Dimulai')
    jadwal_berakhir = models.DateTimeField('Jadwal Berakhir')
    def __str__(self):
        return self.nama_pelajaran

class Mentor(models.Model):
    nama = models.CharField(max_length=200)
    nomor_telepon = models.CharField(max_length=11)
    mata_pelajaran = models.ForeignKey(MataPelajaran, on_delete=models.CASCADE)
    def __str__(self):
        return self.nama
class Challenge(models.Model):
    nama_challenge = models.CharField(max_length=200)
    banyak_soal = models.IntegerField(validators=[MaxValueValidator(8),MinValueValidator(1)])
    bobot_nilai = models.IntegerField(validators=[MaxValueValidator(100),MinValueValidator(0)])
    mata_pelajaran = models.ForeignKey(MataPelajaran, on_delete=models.CASCADE)
    def __str__(self):
        return self.nama_challenge
class LiveCode(models.Model):
    nama_live_code = models.CharField(max_length=200)
    banyak_soal = models.IntegerField(validators=[MaxValueValidator(8),MinValueValidator(1)])
    bobot_nilai = models.IntegerField(validators=[MaxValueValidator(100),MinValueValidator(0)])
    tanggal_pelaksanaan = models.DateField('Tanggal Pelaksanaan')
    mata_pelajaran = models.ForeignKey(MataPelajaran, on_delete=models.CASCADE)
    def __str__(self):
        return self.nama_live_code
