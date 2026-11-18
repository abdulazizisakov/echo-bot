from bot.settings import settings
from bot.updater import Updater


def main() -> None:
    updater = Updater(settings.token)
    updater.start_polling()
