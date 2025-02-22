from django.core.management.base import BaseCommand
from django.core.files import File
from core.models import Newsletter
import os
from django.conf import settings
from datetime import datetime

class Command(BaseCommand):
    help = 'Import existing newsletters from media/newsletters directory'

    def handle(self, *args, **options):
        # First, clear existing newsletters
        Newsletter.objects.all().delete()
        
        newsletters_dir = os.path.join(settings.MEDIA_ROOT, 'newsletters')
        
        for filename in os.listdir(newsletters_dir):
            if filename.endswith('.pdf'):
                try:
                    # Parse date from filename (assuming format: name_YYYY-MM_*.pdf)
                    date_str = filename.split('_')[1]  # Get YYYY-MM part
                    year, month = date_str.split('-')
                    # Create date as first day of the month
                    date = datetime(int(year), int(month), 1)
                    
                    # Create newsletter entry
                    newsletter_path = os.path.join('newsletters', filename)
                    title = filename.replace('.pdf', '').replace('-', ' ')
                    Newsletter.objects.create(
                        title=title,
                        file=newsletter_path,
                        date_created=date,
                        is_published=True
                    )
                    self.stdout.write(
                        self.style.SUCCESS(f'Successfully imported {filename}')
                    )
                except Exception as e:
                    self.stdout.write(
                        self.style.WARNING(f'Failed to import {filename}: {str(e)}')
                    ) 