from django.core.management import BaseCommand

from bot.helpers import set_webhook


class Command(BaseCommand):
    def handle(self, *args, **options):
        is_set, webhook_url = set_webhook()

        if is_set:
            self.stdout.write(self.style.SUCCESS(f"Webhook was successfully set to {webhook_url}"))
        else:
            self.stdout.write(self.style.WARNING(f"Webhook already set to {webhook_url}"))

