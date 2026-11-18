from bot.settings import settings
from bot.updater import Updater
from bot.handlers import TextHandler, PhotoHandler, ContactHandler, LocatioinHandler


def reply_text(update: dict):
    print("text keldi")


def reply_photo(update: dict):
    print("photo keldi")


def reply_contact(update: dict):
    print("contact keldi")


def reply_location(update: dict):
    print("lcoation keldi")


def main() -> None:
    updater = Updater(settings.token)

    updater.dispatcher.add_handler(TextHandler(reply_text))
    updater.dispatcher.add_handler(PhotoHandler(reply_photo))
    updater.dispatcher.add_handler(ContactHandler(reply_contact))
    updater.dispatcher.add_handler(LocatioinHandler(reply_location))

    updater.start_polling()
