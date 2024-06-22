import os
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

# قائمة الأفلام
movies = [
    "Inception",
    "The Dark Knight",
    "Interstellar",
    "Parasite",
    "Joker"
]

# دالة لعرض قائمة الأفلام
def start(update: Update, context: CallbackContext) -> None:
    message = "قائمة الأفلام:\n"
    for movie in movies:
        message += f"- {movie}\n"
    update.message.reply_text(message)

def main() -> None:
    # الحصول على مفتاح API من متغير البيئة
    token = os.getenv('5883022130:AAH2_oaQhNPAEA3hL1OTZ0CtcX7T7ihpQ48')

    updater = Updater(token)

    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))

    updater.start_polling()

    updater.idle()

if __name__ == '__main__':
    main()
