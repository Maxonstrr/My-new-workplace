import telebot
from config import keys,TOKEN
from utils import ConvertionException, CurrencyConverter


bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, f"Приветствую, {message.chat.username}!\n \
Я помогу тебе конвертировать валюту, которая тебе нужна!\n \
К сожалению, я ещё несовершенен и поэтому могу конвертировать лишь некоторые валюты:(\n \
Посмотреть список всех доступных валют: /values\n \
Для подробной информации моей работы:/help")

@bot.message_handler(commands=['help'])
def help(message: telebot.types.Message):
    text = 'Чтобы начать работу введите команду боту в следующем формате: \n<имя валюты, цену которой хотите узнать> \
<имя валюты, в которой надо узнать цену первой валюты> \
<количество переводимой валюты>'
    bot.reply_to(message,text)

@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    text = 'Доступные валюты:'
    for key in keys.keys():
        text = '\n'.join((text, key, ))
    bot.reply_to(message, text)

@bot.message_handler(content_types=['text', ])
def convert(message: telebot.types.Message):
    try:
        values = message.text.lower().split(' ')

        if len(values) > 3:
            raise ConvertionException('Вы ввели слишком много параметров.\n Правила ввода: /values')
        elif len(values) < 3:
            raise ConvertionException('Недостаточно параметров. \n Правила ввода: /values')


        quote, base, amount = values
        total_base = CurrencyConverter.get_price(quote, base, amount)
    except ConvertionException as e:
        bot.reply_to(message, f'Ошибка пользователя.\n{e}')
    except Exception as e:
        bot.reply_to(message, f'Не удалось обработать команду\n{e}')
    else:
        text = f'Цена {amount} {quote} в {base} - {total_base}'
        bot.send_message(message.chat.id, text)

bot.polling()