from django.contrib.auth import get_user_model
from django.core.management import CommandError
from django.core.management.base import BaseCommand
from django.db import transaction


class Command(BaseCommand):
    help = "Create superadmin user, at doc)ker startup, if it doesn't exist"

    def add_arguments(self, parser):
        parser.add_argument("--username", help="Username")
        parser.add_argument("--email", help="Email")
        parser.add_argument("--password", help="Password")

    def handle(self, *args, **options):

        user = get_user_model()

        if "username" not in options or "email" not in options or "password" not in options:
            raise CommandError("Username, email and password are required")
        
        if not user.objects.filter(username=options["username"]).exists():
            with transaction.atomic():
                user = user.objects.create_superuser(
                    username=options["username"], email=options["email"], password=options["password"]
                )
        else:
            self.stdout.write(self.style.ERROR('Superuser already exists'))