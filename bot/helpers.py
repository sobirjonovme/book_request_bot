import requests
from django.conf import settings
from django.urls import reverse


def generate_webhook_url():
    host: str = settings.HOST
    if host.endswith("/"):
        host = host[:-1]
    return host + reverse(settings.BOT_WEBHOOK_PATH, args=(settings.BOT_TOKEN,))


def get_webhook_url():
    url = "https://api.telegram.org/bot5060653181:AAGYXXcL4VvPLXuc8cz2Ec9AHgG6fMUjsRg/getWebhookInfo"
    response = requests.get(url)
    if response.status_code != 200:
        return None

    webhook_url = response.json().get("result", {}).get("url", None)
    return webhook_url


def set_webhook():
    current_webhook_url = get_webhook_url()
    webhook_url = generate_webhook_url()

    if current_webhook_url != webhook_url:
        url = "https://api.telegram.org/bot5060653181:AAGYXXcL4VvPLXuc8cz2Ec9AHgG6fMUjsRg/setWebhook"
        params = {
            "url": webhook_url
        }
        requests.get(url, params=params)
        return True, webhook_url

    return False, current_webhook_url
