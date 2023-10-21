import telebot


bot = telebot.TeleBot("6637498364:AAGKW-QFMuoUofd_yf-pm1jHxbWhTq7efnU")

commands = [
    {'command': 'start', 'description': 'Start the bot'},
    {'command': 'help', 'description': 'Get help'},
    {'command': 'helloworld', 'description': 'Say Hello World'},
]

# bot.set_my_commands(commands=commands)
bot.send_message()
# bot.set_my_commands()


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Howdy, how are you doing?")


bot.infinity_polling()
