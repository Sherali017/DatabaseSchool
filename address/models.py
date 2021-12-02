from django.db import models


class VilAddressModel(models.Model):
    vil = models.CharField(max_length=255)

    def __str__(self):
        return self.vil

    class Meta:
        verbose_name = 'viloyat'
        verbose_name_plural = 'viloyatlar'


class TShAddressModel(models.Model):
    tum_shah = models.CharField(max_length=255)

    def __str__(self):
        return self.tum_shah

    class Meta:
        verbose_name = 'Tuman va shahar'
        verbose_name_plural = 'tumanlar va shaharlar'


class SchoolAddressModel(models.Model):
    mak = models.CharField(max_length=255)

    def __str__(self):
        return self.mak

    class Meta:
        verbose_name = 'Maktab manzili'
        verbose_name_plural = 'maktab manzillari'


class SchoolModel(models.Model):
    vil = models.OneToOneField(VilAddressModel, on_delete=models.CASCADE)
    tum_sh = models.OneToOneField(TShAddressModel, on_delete=models.CASCADE)
    address = models.OneToOneField(SchoolAddressModel, on_delete=models.CASCADE)

    school_name = models.CharField(max_length=255)
    school_principal = models.CharField(max_length=255)
    school_details = models.TextField()

    def __str__(self):
        return f'{self.vil} {self.tum_sh} {self.address} {self.school_name}'

    class Meta:
        verbose_name = 'maktab'
        verbose_name_plural = 'maktablar'
