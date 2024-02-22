from django.apps import AppConfig


class BotConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'bot'

    def ready(self):
        from bot.helpers import set_webhook

        is_set, webhook_url = set_webhook()

        if is_set:
            print(f"Webhook was successfully set to {webhook_url}")
        else:
            print(f"Webhook already set to {webhook_url}")