from django.core.management.base import BaseCommand
from school.models import University
import pycountry
import csv

class Command(BaseCommand):
    help = 'Importation des universite depuis le fichier CSV'

    def handle(self, **args):
        with open('./world-universities.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                country_code, name, website = row 

                country = pycountry.countries.get(alpha_2=country_code)
                country_name = country.name if country else "Unknow"
                
                # Save University in the database
                University.objects.get_or_create(
                    country_code = country_code,
                    country_name = country_code,
                    name = name,
                    website = website
                )
                self.stdout.write(self.style.SUCCESS('Importation reussi'))
