from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CallbackQueryHandler, ConversationHandler, MessageHandler, BaseFilter

from models import find_chanel_by_chat

COUNTRIES = (
    (u'Украина', 'set_country.ua'),
    (u'Россия', 'set_country.ru'),
    (u'Белоруссия', 'set_country.by'),
    (u'Казахстан', 'set_country.kz'),
)


def build_keyboard(country_list):
    countries = []
    for (country, callback) in country_list:
        country_keyboard = [InlineKeyboardButton(country, callback_data=callback)]
        countries.append(country_keyboard)

    return countries


def show_all(bot, update):
    reply_markup = InlineKeyboardMarkup(build_keyboard(COUNTRIES))
    update.message.reply_text(u"Выберите страну для поиска", reply_markup=reply_markup)


def save_country(bot, update):
    print(update)
    selected_country = update.callback_query.data.split('.')[1] or 'ru'

    query = update.callback_query

    chanel = find_chanel_by_chat(query.message.chat)
    chanel.set_country(selected_country)

    # keyboard = [[InlineKeyboardButton(u"Ок", callback_data='_')]]
    # reply_markup = InlineKeyboardMarkup(keyboard)

    bot.sendMessage(
        chat_id=query.message.chat_id,
        text=u"Данные сохранены."
    )



def complete(bot, update):
    query = update.callback_query

    bot.edit_message_text(
        chat_id=query.message.chat_id,
        message_id=query.message.message_id,
        text=u"Готово."
    )


class CountryFilter(BaseFilter):
    def filter(self, message):
        return 'Указать страну' in message.text


country_handler = ConversationHandler(
    entry_points=[MessageHandler(CountryFilter(), show_all)],
    states={
        'SAVE_COUNTRY': [CallbackQueryHandler(save_country)],
        'COMPLETE': [CallbackQueryHandler(complete)],
    },
    fallbacks=[],
    allow_reentry=True
)

if __name__ == '__main__':
    updater = Updater('403877811:AAFjD7RbEnRrNTQkqLyBOxQhx7OAnMpBc8Q')

    updater.dispatcher.add_handler(country_handler)
    updater.start_polling()
    updater.idle()
