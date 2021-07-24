from django.core.management.base import BaseCommand, CommandError
import logging


class Command(BaseCommand):
    help = "create superuser"

    def handle(self, *args, **options):
        from django.contrib.auth.models import User

        logger = logging.getLogger()
        if not User.objects.filter(is_superuser=True).exists():
            User.objects.create_superuser("admin", "admin@example.com", "adminpass")
            logger.msg = "Done creating user"
            print("Done creating user")
        else:
            logger.msg = "User Exists"
            print("User Exists")
