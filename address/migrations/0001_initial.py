# Generated by Django 3.2.9 on 2021-12-02 06:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SchoolAddressModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mak', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Maktab manzili',
                'verbose_name_plural': 'maktab manzillari',
            },
        ),
        migrations.CreateModel(
            name='TShAddressModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tum_shah', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Tuman va shahar',
                'verbose_name_plural': 'tumanlar va shaharlar',
            },
        ),
        migrations.CreateModel(
            name='VilAddressModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vil', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'viloyat',
                'verbose_name_plural': 'viloyatlar',
            },
        ),
        migrations.CreateModel(
            name='SchoolModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('school_name', models.CharField(max_length=255)),
                ('school_principal', models.CharField(max_length=255)),
                ('school_details', models.TextField()),
                ('address', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='address.schooladdressmodel')),
                ('tum_sh', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='address.tshaddressmodel')),
                ('vil', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='address.viladdressmodel')),
            ],
            options={
                'verbose_name': 'maktab',
                'verbose_name_plural': 'maktablar',
            },
        ),
    ]
