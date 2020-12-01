import telebot
import confige
import parse
import parse_bsuir
from telebot import types

client = telebot.TeleBot(confige.config['token'])

@client.message_handler(commands=['start'])
def button(message):
    markup_inline = types.InlineKeyboardMarkup()
    item_yes = types.InlineKeyboardButton(text='ДА', callback_data='yes')
    item_no = types.InlineKeyboardButton(text='НЕТ', callback_data='no')

    markup_inline.add(item_yes, item_no)
    client.send_message(message.chat.id, 'Привет. Начнем работу?',
    reply_markup=markup_inline
    )


@client.callback_query_handler(func=lambda call: True)
def callback(call):
    if call.data == 'yes':
        markup_reply = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item_weather = types.KeyboardButton('Погода')
        item_schedule = types.KeyboardButton('Рассписание')
        item_teacher = types.KeyboardButton('Преподаватель')

        markup_reply.add(item_weather, item_schedule, item_teacher)
        client.send_message(call.message.chat.id, 'Информацию о чем вы хотите получить?',
        reply_markup=markup_reply
        )
    elif call.data == 'no':
        client.send_message(call.message.chat.id, 'Очень жаль! возвращайтесь еще!')

@client.message_handler(content_types=['text'])
def get_info(message):
    global fio
    if message.text == 'Бот, расскажи о себе':
        client.send_message(message.chat.id,'Добро пожаловать в телеграм-бот Leps0n.\n\n С помощью данного бота вы сможете\n 1. Узнать погоду на сегодня\n 2. Рассписание занятий на сегодня\n 3. Информаию о преподавателе.\n\n Для начала работы напишите "/start"')
    elif message.text == 'Погода':
        client.send_message(message.chat.id, parse.parse())
    elif message.text == 'Рассписание':
        client.send_message(message.chat.id, parse_bsuir.parse_schedule())
    elif message.text == 'Преподаватель':
        client.send_message(message.chat.id, 'Введите ФИО преподавателя \n(Пример: Анисимов Владимир Яковлевич)')
    else:
        client.send_message(message.chat.id, 'Я не знаю этой команды:(\nЕсли хочешь узнать мой функционал, напиши мне "Бот, расскажи о себе"')

client.polling(none_stop=True, interval=0)
