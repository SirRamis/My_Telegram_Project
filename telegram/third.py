# Добовляем кнопки в телеграмм бот

import telebot
import random
from telebot import types

token = "6280256013:AAFxiErfho7BYdIwMp7gXva1xgacj4vlW60"
photo_url = 'https://kuku.travel/wp-content/uploads/2018/05/%D0%91%D1%83%D1%80%D1%81%D0%B0-%D0%A2%D1%83%D1%80%D1%86%D0%B8%D1%8F.jpg'
bot = telebot.TeleBot(token)

RANDOM_TASKS = ["Почитать Коран сегодня", "Сделать зикр сегодня", "Позвонить родственникам сегодня", "Сделать дога сегодня"]
RANDOM_TASKS_2 = ["rr", "tt"]
tasks = []
todos = dict() # todos = {}
todos = list() # todos = []
#Добавили кнопки
@bot.message_handler(commands=["start"])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton('Время с пользой')
    item2 = types.KeyboardButton('Хадис')
    item3 = types.KeyboardButton('Просмотр задач')
    item4 = types.KeyboardButton('Информация')

    markup.add(item1, item2, item3, item4)

    bot.send_message(message.chat.id, f"Ассаляму алейкум {message.from_user.first_name}!", reply_markup=markup)

@bot.message_handler(commands=[])
def show(message):
    command = message.text
    date = command
    text = ""
    if date in tasks:
        text = date.append() + "\n"
        for task in tasks:
            text = text + "-" + task + "\n"
    else:
        text = "Задач на эту дату нет"
    bot.send_message(message.chat.id, text) # отправляем сообщение с текстом результатом
    return text # возвращаем текст результата


#Добавляем тексты на кнопки
@bot.message_handler(content_types=["text"])
def bot_message(message):
    if message.chat.type == 'private':
        if message.text == 'Время с пользой':
            task = random.choice(RANDOM_TASKS)
            text = "Задача " + task + " добавлена на сегодня "
            todos.append(task)
            bot.send_message(message.chat.id, text)
        elif message.text == 'Хадис':
            task = random.choice(RANDOM_TASKS_2)
            bot.send_message(message.chat.id, task)
        elif message.text == 'Просмотр задач':
            text = show(message)
            bot.send_message(message.chat.id, text)
        elif message.text == 'Информация':#Пеедаем картинку
            bot.send_photo(message.chat.id, photo=photo_url, caption='ассаляму алейкум !как хэллэр?')



#@bot.message_handler(commands=["add"])
#def add(message):
#    markup = types.InlineKeyboardMarkup(row_width=1)
#    iy = types.InlineKeyboardButton('добавь задачу', callback_data='que_1')
#    markup.add(iy)

#    bot.send_message(message.chat.id, f"Привет {message.from_user.first_name}!", reply_markup=markup)


#@bot.callback_query_handler(func=lambda call: True)
#def callback(call):
#    if call.message:
#        if call.data == 'que_1':
#            task = random.choice(RANDOM_TASKS)
#            text = "Задача " + task + " добавлена на сегодня "
#            bot.send_message(call.message.chat.id, text)


bot.polling(none_stop=True)
