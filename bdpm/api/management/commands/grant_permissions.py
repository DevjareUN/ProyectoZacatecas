# myapp/management/commands/grant_permissions.py

from django.core.management.base import BaseCommand
from django.db import connection

class Command(BaseCommand):
    help = 'Grants permissions to user for database usage'

    def handle(self, *args, **options):
        with connection.cursor() as cursor:
            cursor.execute("GRANT ALL PRIVILEGES ON DATABASE bdpm TO pgadmin;")

