from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    def handle(self, *args, **options):
        User = get_user_model()
        if not User.objects.filter(username="admin").exists():
            #  change the username, email and password before use
            #   it is recomended to use environment variables for this to avoid pushing sensitive 
            #      info in remote repository
            User.objects.create_superuser("admin", "admin@xyzdomain.com", "admin123")
            self.stdout.write(self.style.SUCCESS("admin user has created"))
        else:
            self.stdout.write(self.style.SUCCESS("admin user already exists"))
