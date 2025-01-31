from config import TOKEN
import telebot
import random
API_TOKEN = TOKEN

bot = telebot.TeleBot(API_TOKEN)

class Car:
    def __init__(self, color, brand):
        self.color = color
        self.brand = brand
    def info(self):
        return f'Марка: {self.brand}, Цвет: {self.color}' # f позволяет удобнее записать и текст и переменные


    
# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, """\
Hi there, I am EchoBot.
I am here to echo your kind words back to you. Just say anything nice and I'll say the exact same thing to you!\
""")


quote = ['Живи так, как если бы тебе предстояло умереть завтра. Учись так, как будто тебе суждено жить вечно (Махатма Ганди).','День без улыбки — потерянный день (Чарльз Спенсер (Чарли) Чаплин).','Быть счастливым — это не цель и не приобретенное благо. Это решение (Карлос Сантана).','Хорошие друзья, хорошие книги и спящая совесть — вот идеальная жизнь (Марк Твен).']

@bot.message_handler(commands=['info'])
def command(message):
    bot.send_message(message.chat.id, "Этот бот был создан 25 января 2025 года")

@bot.message_handler(commands=['quote'])
def command(message):
    bot.send_message(message.chat.id, random.choice(quote))

@bot.message_handler(content_types=['photo'])
def handle_docs_photo(message):
    bot.send_message(message.chat.id, 'Крутая фотка')

@bot.message_handler(commands=['car'])
def hadle_car_command(message):

    msg_text = message.text[len('/car '):].strip()  # Получаем текст после команды /car отсекает кол-во символов равное кол-ву символов в слове /car и удаляет после него все знаки (пробелы, запятые и т.д.)

    # Разделяем текст на части
    args = msg_text.split(maxsplit=1) # строка может разделиться только на 2
    
    color = args[0]
    brand = args[1]

    car = Car(color, brand)

    bot.reply_to(message, car.info())


    



# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
#@bot.message_handler(func=lambda message: True)
#def echo_message(message):
    #bot.reply_to(message, message.text)


bot.infinity_polling()

