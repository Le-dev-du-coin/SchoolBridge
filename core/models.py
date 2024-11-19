from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone


class User(AbstractUser):
    username = models.CharField(verbose_name="Nom d'utilisateur", max_length=60)
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
    REQUIRED_FIELDS = ["username", "first_name", "last_name"]

    class Meta:
        verbose_name = 'Utilisateur'
        verbose_name_plural = 'Utilisateurs'

    def __str__(self):
        return self.get_full_name()


class OnetimePasscode(models.Model):
    user = models.OneToOneField(User, verbose_name="Utilisateur", on_delete=models.CASCADE)
    code = models.CharField(verbose_name="Code OTP", max_length=6)
    created_at = models.DateTimeField(auto_now_add=True)

    def is_valid(self):
        return (timezone.now() - self.created_at).total_seconds() < 120

    def __str__(self):
        return f"{self.user.email} - Code OTP: {self.code}"