from django.db import models

class University(models.Model):
    '''Model definition for School.'''
    name = models.CharField(name='Nom de l\'ecole', max_length=100)
    coutry_code = models.CharField(name='Code du pays', max_length=3)
    country_name = models.CharField(name='Pays', max_length=120, null=True, blank=True)
    city = models.CharField(name='Ville', max_length=120, null=True, blank=True)
    domain = models.CharField(name='Domaine d\'etude', max_length=120, null=True, blank=True)
    min_level = models.DecimalField(name='Niveau minimum', decimal_places=3, null=True, blank=True),
    require_score = models.DecimalField(name='Score requis', decimal_places=3, max_digits=3, null=True, blank=True)
    documents_fees = models.CharField(name='Frais de dossier', max_length=60, null=True, blank=True)

    class Meta:
        '''Meta definition for School.'''

        verbose_name = 'Université'
        verbose_name_plural = 'Universités'

    def __str__(self):
        return f'{self.name}' # Add change later



class Candidate(models.Model):
    pass


class Documents(models.Model):
    pass

class Message(models.Model):
    pass