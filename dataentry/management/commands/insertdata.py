# This code is a custom Django management command. It allows to avoid entering data manually through the admin panel; 
# instead, you can load it all at once using a single command: python manage.py insertdata. / 
# Этот код — кастомная консольная команда Django. 
# Она позволяет не вводить данные вручную через админку, а загружать их одной командой python manage.py insertdata.

from django.core.management.base import BaseCommand # This imports the base class needed to create own manage.py command / Базовый класс, от которого строятся все команды Django
from dataentry.models import Student # This tells the script which database table (Model) to work with / В какую именно таблицу (модель) будем сохранять данные.

# I want to add some data to the database using the custom command

class Command(BaseCommand) :
    help = "it will insert data to the database" #This is just a description of what the command does.

    def handle(self, *args, **kwargs):
        # logic goes here
        dataset = [
            {'roll_no': 1002, 'name': 'Sachin', 'age':21},
            {'roll_no': 1006, 'name': 'Michel', 'age':22},
            {'roll_no': 1004, 'name': 'Mike', 'age':23},
            {'roll_no': 1010, 'name': 'Anna', 'age':20},
        ]
        
        for data in dataset: # Pick the first student from the list
            roll_no = data['roll_no'] # Extract the ID number
            existing_record = Student.objects.filter(roll_no=roll_no).exists() # Ask the database: "Do you already have a student with this number?"
           
            if not existing_record:
                Student.objects.create(roll_no=data['roll_no'], name=data['name'], age=data['age'])
            else: 
                self.stdout.write(self.style.WARNING(f'Student with roll no {roll_no} already exists!'))
        self.stdout.write(self.style.SUCCESS('Data inserted successefully'))