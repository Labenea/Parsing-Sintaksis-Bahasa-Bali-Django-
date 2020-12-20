from django.db import models

# Create your models here.


class K(models.Model):
    rules = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'K'
        verbose_name_plural = 'K'

    def __str__(self):
        return self.rules


class S(models.Model):
    rules = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'S'
        verbose_name_plural = 'S'

    def __str__(self):
        return self.rules


class P(models.Model):
    rules = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'P'
        verbose_name_plural = 'P'

    def __str__(self):
        return self.rules


class O(models.Model):
    rules = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'O'
        verbose_name_plural = 'O'

    def __str__(self):
        return self.rules


class Pel(models.Model):
    rules = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'Pel'
        verbose_name_plural = 'Pel'

    def __str__(self):
        return self.rules


class Ket(models.Model):
    rules = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'Ket'
        verbose_name_plural = 'Ket'

    def __str__(self):
        return self.rules


class FN(models.Model):
    rules = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'FN'
        verbose_name_plural = 'FN'

    def __str__(self):
        return self.rules


class FV(models.Model):
    rules = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'FV'
        verbose_name_plural = 'FV'

    def __str__(self):
        return self.rules


class FS(models.Model):
    rules = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'FS'
        verbose_name_plural = 'FS'

    def __str__(self):
        return self.rules


class Gt(models.Model):
    rules = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'Gt'
        verbose_name_plural = 'Gt'

    def __str__(self):
        return self.rules


class Pn(models.Model):
    rules = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'Pn'
        verbose_name_plural = 'Pn'

    def __str__(self):
        return self.rules


class Ps(models.Model):
    rules = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'Ps'
        verbose_name_plural = 'Ps'

    def __str__(self):
        return self.rules


class Pr(models.Model):
    rules = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'Pr'
        verbose_name_plural = 'Pr'

    def __str__(self):
        return self.rules


class Kt(models.Model):
    rules = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'Kt'
        verbose_name_plural = 'Kt'

    def __str__(self):
        return self.rules
