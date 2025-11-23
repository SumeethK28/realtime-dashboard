from django.core.management.base import BaseCommand
from dashboard_app.data_generator_advanced import run_advanced_data_simulation

class Command(BaseCommand):
    help = 'Starts generating simulated real-time data from 7 different sources'
    
    def handle(self, *args, **options):
        self.stdout.write(
            self.style.SUCCESS('Starting ADVANCED real-time data generation...')
        )
        run_advanced_data_simulation()