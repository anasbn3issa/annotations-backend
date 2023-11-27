from django.core.management.base import BaseCommand
from app.models import Annotation

class Command(BaseCommand):
    help = 'Clears the database of all labels and annotations'

    def handle(self, *args, **options):
        # Delete all annotations
        Annotation.objects.all().delete()

        self.stdout.write(self.style.SUCCESS('Annotations cleared successfully'))
