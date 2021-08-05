import telebot
from telebot import types
from config import token


bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.from_user.id, 'Привет, давай познакомимся! Как тебя зовут?')
    bot.register_next_step_handler(message, reg_name)


def reg_name(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    markup.row('Прекрасно', 'Нормально')
    #markup.row('Нормально')
    markup.row('Так себе', 'Болею')
    #markup.row('Болею')
    markup.row('Хочу в отпуск!!!')
    bot.send_message(message.from_user.id, 'как ты себя чувствуешь на этой неделе?', reply_markup=markup)



@bot.message_handler(content_types=['text'])
def text(message):
    if message.text == 'Прекрасно':
        bot.send_message(message.chat.id, "Супир! Давай же скорее сделаем VIGBO самым крутым продуктом!")
    elif message.text == 'Нормально':
        bot.send_message(message.chat.id, "Мотивирующий текст")
    elif message.text == 'Так себе':
        bot.send_message(message.chat.id,  "Напиши эйчару @Ksenya_zh, она поможет")
    elif message.text == 'Болею':
        bot.send_message(message.chat.id, "ссылка на регламент sick days, http://www.ems.by/")
    elif message.text == 'Хочу в отпуск!!!':
        bot.send_message(message.chat.id, "ссылка на статью про work-life и на регламент согласования отпуска")








bot.polling(none_stop=True)
