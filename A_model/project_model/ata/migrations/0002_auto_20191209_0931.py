# Generated by Django 3.0 on 2019-12-09 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ata', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='matapelajaran',
            name='jadwal_berakhir',
            field=models.DateTimeField(verbose_name='Jadwal Berakhir'),
        ),
        migrations.AlterField(
            model_name='matapelajaran',
            name='jadwal_dimulai',
            field=models.DateTimeField(verbose_name='Jadwal Dimulai'),
        ),
    ]