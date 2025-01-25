from config import TOKEN
import telebot

API_TOKEN = TOKEN

bot = telebot.TeleBot(API_TOKEN)


# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, """\
Hi there, I am EchoBot.
I am here to echo your kind words back to you. Just say anything nice and I'll say the exact same thing to you!\
""")


@bot.message_handler(commands=['info'])
def command(message):
    bot.send_message(message.chat.id, "Этот бот был создан 25 января 2025 года")


@bot.message_handler(content_types=['photo'])
def handle_docs_photo(message):
    bot.send_message(message.chat.id, 'Крутая фотка')



# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
#@bot.message_handler(func=lambda message: True)
#def echo_message(message):
    #bot.reply_to(message, message.text)


bot.infinity_polling()

