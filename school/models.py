from djmoney.models.fields import MoneyField
from django.db import models

class University(models.Model):
    '''Model definition for School.'''
    name = models.CharField(verbose_name="Nom de l'ecole", max_length=100)
    country_code = models.CharField(verbose_name="Code du pays", max_length=3)
    country_name = models.CharField(verbose_name="Pays", max_length=120)
    city = models.CharField(verbose_name="Ville", max_length=120, null=True, blank=True)
    website = models.URLField(verbose_name="Site Web", max_length=100)
    domain = models.CharField(verbose_name="Domaine d'etude", max_length=120, null=True, blank=True)
    edu_level_required = models.CharField(verbose_name="Niveau requis", max_length=120, null=True, blank=True)
    require_score = models.DecimalField(verbose_name="Score requis", default=0.0, decimal_places=2, max_digits=4, null=True, blank=True)
    documents_fees = MoneyField(verbose_name="Frais de dossier", decimal_places=0, max_digits=10, default_currency="XOF", null=True, blank=True)
    image = models.ImageField(verbose_name="Image")

    class Meta:
        '''Meta definition for School.'''

        verbose_name = 'Université'
        verbose_name_plural = 'Universités'

    def __str__(self):
        return f"Univertite: {self.name}" # Add change later


class Programs(models.Model):
    '''Model definition for Programs.'''
    name = models.CharField(verbose_name="Nom", max_length=120)
    duration = models.CharField(verbose_name="Durée", max_length=60)
    degree = models.CharField(verbose_name="Niveau", max_length=120)
    university = models.ForeignKey(
        "University", 
        verbose_name="Université", 
        on_delete=models.CASCADE, 
        related_name="programs"
    )  # Relation ve
    class Meta:
        '''Meta definition for Programs.'''

        verbose_name = 'Programme'
        verbose_name_plural = 'Programmes'

    def __str__(self):
        return f"{self.name} {self.university.name}"


class Candidate(models.Model):
    pass


class Documents(models.Model):
    pass

class Message(models.Model):
    pass