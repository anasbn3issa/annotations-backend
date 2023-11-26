from django.core.management.base import BaseCommand
from app.models import Label, Annotation

class Command(BaseCommand):
    help = 'Clears the database of all labels and annotations'

    def handle(self, *args, **options):
        # Delete all labels and annotations
        Label.objects.all().delete()
        Annotation.objects.all().delete()

        self.stdout.write(self.style.SUCCESS('Database cleared successfully'))
