from django.db import models
from core.models import User


class Student(models.Model):
    '''Model definition for Student.'''

    user = models.OneToOneField(User, verbose_name="Utilisateur", on_delete=models.CASCADE, related_name="student_profile")
    date_of_birth = models.DateField(name="Date de naissance", null=True, blank=True)
    country_origin = models.CharField(name="Pays d'origine", max_length=100, null=True, blank=True)
    phone_number = models.CharField(verbose_name="Numero de téléphone", max_length=8, null=True, blank=True)
    education_level = models.CharField(name="Niveau d'etude", max_length=100, null=True, blank=True)
    bac_serie = models.CharField(name="Serie BAC", max_length=100, null=True, blank=True) # After change to choices
    average_score  = models.DecimalField(name="Score moyen", decimal_places=2, max_digits=4, null=True, blank=True)


    class Meta:
        '''Meta definition for Student.'''

        verbose_name = "Étudiant"
        verbose_name_plural = "Étudiants"
    
    def __str__(self):
        return f"Profil Étudiant: {self.user.get_full_name()}"
