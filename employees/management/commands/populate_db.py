from django.core.management.base import BaseCommand
from employees.models import Employee, Idea
from faker import Faker

class Command(BaseCommand):
    help = 'Populate the database with initial data'

    def add_arguments(self, parser):
        parser.add_argument('num_records', type=int, help='Indicates the number of records to create')

    def handle(self, *args, **options):
        num_records = options['num_records']
        fake = Faker()

        for _ in range(num_records):
            Employee.objects.create(
                fullname=fake.name(),
                dep=fake.job(),
                birthdate=fake.date_of_birth(minimum_age=18, maximum_age=65).strftime('%Y-%m-%d'),
                salary=str(fake.random_number(digits=6))
            )
            Idea.objects.create(
                userName=fake.name(),
                idea=fake.sentence(nb_words=10)
            )
        
        self.stdout.write(self.style.SUCCESS(f'{num_records} records created successfully'))
