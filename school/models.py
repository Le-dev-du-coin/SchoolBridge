from django.db import models

class University(models.Model):
    '''Model definition for School.'''
    name = models.CharField(verbose_name='Nom de l\'ecole', max_length=100)
    country_code = models.CharField(verbose_name='Code du pays', max_length=3)
    country_name = models.CharField(verbose_name='Pays', max_length=120)
    city = models.CharField(verbose_name='Ville', max_length=120, null=True, blank=True)
    website = models.URLField(verbose_name="Site Web", max_length=100)
    domain = models.CharField(verbose_name='Domaine d\'etude', max_length=120, null=True, blank=True)
    min_level = models.DecimalField(verbose_name='Niveau minimum', decimal_places=3, null=True, blank=True),
    require_score = models.DecimalField(verbose_name='Score requis', decimal_places=3, max_digits=3, null=True, blank=True)
    documents_fees = models.CharField(verbose_name='Frais de dossier', max_length=60, null=True, blank=True)

    class Meta:
        '''Meta definition for School.'''

        verbose_name = 'Université'
        verbose_name_plural = 'Universités'

    def __str__(self):
        return f'Univertite: {self.name}' # Add change later



class Candidate(models.Model):
    pass


class Documents(models.Model):
    pass

class Message(models.Model):
    pass