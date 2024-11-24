from django.db import models
from core.models import User
from django_countries.fields import CountryField


class Student(models.Model):
    '''Model definition for Student.'''

    EDUCATION_LEVEL = [
    ("bac", "BAC"),
    ("licence", "Licence"),
    ("master", "Master"),
    ("doctorat", "Doctorat"),
    ("cap", "CAP"),
    ]

    BAC_SERIES = [
        ("tll", "Terminale Lettre et Littérature (TLL)"),
        ("tseco", "Terminale Science Économique (TSECO)"),
        ("tss", "Terminale Science Exacte (TSS)"),
    ]

    user = models.OneToOneField(
        User, verbose_name="Utilisateur", on_delete=models.CASCADE, related_name="student_profile"
    )
    profile_picture = models.ImageField(verbose_name="Image de profil", null=True, blank=True)
    date_of_birth = models.DateField(verbose_name="Date de naissance", null=True, blank=True)
    country_origin = models.CharField(verbose_name="Pays d'origine", max_length=100, null=True, blank=True)
    phone_number = models.CharField(verbose_name="Numéro de téléphone", max_length=15, null=True, blank=True)
    education_level = models.CharField(
        choices=EDUCATION_LEVEL, verbose_name="Niveau d'étude", max_length=100, null=True, blank=True
        )
    bac_serie = models.CharField(
        choices=BAC_SERIES, verbose_name="Série BAC", max_length=60, null=True, blank=True
    )
    average_score = models.DecimalField(
        verbose_name="Score moyen", default=0.0, decimal_places=2, max_digits=4, null=True, blank=True
    )

    class Meta:
        verbose_name = "Étudiant"
        verbose_name_plural = "Étudiants"

    def __str__(self):
        return f"Profil Étudiant: {self.user.get_full_name()}"


class Country_wishlist(models.Model):
    '''Model definition for Country_wishlist.'''
    name = models.CharField(max_length=60)
    student = models.ForeignKey("Student", verbose_name="Etudiant", related_name="wishlist", on_delete=models.CASCADE)
    class Meta:
        '''Meta definition for Country_wishlist.'''

        verbose_name = 'Pays Favoris'
        verbose_name_plural = 'Pays Favoris'

    def __str__(self):
        return self.name