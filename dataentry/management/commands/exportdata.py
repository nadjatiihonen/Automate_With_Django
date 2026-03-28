import csv
from django.core.management.base import BaseCommand
from dataentry.models import Student

# proposed command = pyton manage.py exportdata / предложенная команда
class Command(BaseCommand):
    help = 'Export data from Student model tp a CSV file'

    def handle(self, *args, **kwargs):
        # fetch the data feom the dtabase / получить данные из базы данных


        # define the csv file/name / указать CSV-файл / имя файла


        # open the csv file and write the data