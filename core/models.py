from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    first_name = models.CharField(verbose_name="Prénom", max_length=60)
    last_name = models.CharField(verbose_name="Nom", max_length=60)
    email = models.EmailField(verbose_name="Adresse email", unique=True)
    is_student = models.BooleanField(verbose_name="Est_Etudiant", default=False, null=True, blank=True)
    is_superuser = models.BooleanField(verbose_name="Est_SuperAdmin", default=False, null=True, blank=True)
    is_active = models.BooleanField(verbose_name="Est_active", default=True)
    is_validated = models.BooleanField(verbose_name="Est_validé", default=False, null=True, blank=True)
    date_joined = models.DateTimeField(verbose_name="Date d'inscription", auto_now_add=True)
    last_login = models.DateTimeField(verbose_name="Dernière connexion", auto_now=True)
    
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name"]

    class Meta:
        verbose_name = 'Utilisateur'
        verbose_name_plural = 'Utilisateurs'

    def __str__(self):
        return f"{self.first_name} {self.last_name}"