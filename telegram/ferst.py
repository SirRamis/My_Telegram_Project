#Добовляем кнопки в телеграмм бот

import telebot
import random
from telebot import types

token = "6280256013:AAFxiErfho7BYdIwMp7gXva1xgacj4vlW60"

bot = telebot.TeleBot(token)

RANDOM_TASKS = ["Почитать Коран", "Сделать зикр", "Позвонить родственникам", "Сделать дога"]

@bot.message_handler(commands=["add"])
def add(message):
    markup = types.InlineKeyboardMarkup(row_width=1)
    iy = types.InlineKeyboardButton('добавь задачу', callback_data='que_1')
    markup.add(iy)

    bot.send_message(message.chat.id, "привет", reply_markup=markup)

@bot.message_handler(commands=["random"])
def random_add(message):
    task = random.choice(RANDOM_TASKS)
    text = "Задача " + task + " добавлена на сегодня "
    bot.send_message(message.chat.id, text)

@bot.callback_query_handler(func=lambda call:True)
def callback(call):
    if call.message:
        if call.data == 'que_1':
            task = random.choice(RANDOM_TASKS)
            text = "Задача " + task + " добавлена на сегодня "
            bot.send_message(call.message.chat.id, text)


bot.polling(none_stop=True)