import telebot
from telebot import types

bot = telebot.TeleBot('5076105120:AAGr0wRSdJUEOEsZTxp3JOL33PYLsGsvxQg')


@bot.message_handler(commands=['start'])
def start(message):
    keyboard = types.ReplyKeyboardMarkup()
    keyboard.row("Хочу узнать о МТУСИ", "Больше", "/help", "/timetable")
    bot.send_message(message.chat.id, 'Привет! Хочешь узнать свежую информацию?', reply_markup=keyboard)


@bot.message_handler(commands=['help'])
def start_message(message):
    bot.send_message(message.chat.id, 'Я много чего умею и много чего не умею, но я не перестаю быть самым крутым '
                                      'ботом!\n'
                                      'Я могу выполнять следующие команды:\n'
                                      'Команда /start - начало работы\n'
                                      'Команда /help - вызывает перечень команд\n'
                                      'Команда /timetable - выдаёт ссылку на сайт расписания МТУСИ\n'
                                      'Также есть список текстовых команд:\n'
                                      'Напишите в чат: "Хочу узнать о МТУСИ" - и зайдете на официальный сайт\n'
                                      'Напишите в чат: "Больше новостей" - и сможете узнать больше новостей\n'
                                      'Напишите в чат: "Больше настроения" - и можете перейти на сайт анекдотами\n')


@bot.message_handler(commands=['timetable'])
def start_message(message):
    bot.send_message(message.chat.id, 'Расписание - https://mtuci.ru/time-table/')


@bot.message_handler(content_types=['text'])
def answer(message):
    if message.text.lower() == "хочу узнать о мтуси":
        bot.send_message(message.chat.id, 'Тогда тебе сюда – https://mtuci.ru/')
    elif message.text.lower() == "больше":
        bot.send_message(message.chat.id, 'Чего больше то?')
    elif message.text.lower() == "больше новостей":
        bot.send_message(message.chat.id, 'Лааадно! Лови ссылку - https://ria.ru/world/')
    elif message.text.lower() == "больше настроения":
        bot.send_message(message.chat.id, 'Чего такой грустный? Лови ссылку - https://anekdotov.net/anekdot/')
    else:
        bot.send_message(message.chat.id, 'Я вас не понял!')


bot.polling(none_stop=True, interval=0)
