from django.core.management import BaseCommand

from notes.services import create_default_categories


class Command(BaseCommand):

    def handle(self, *args, **options):
        create_default_categories()
