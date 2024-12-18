import telebot

bot = telebot.TeleBot('TOKEN')

@bot.message_handler(commands=['start','help'])
def main(message):
    bot.send_message(message.chat.id, f'Привет  {message.from_user.first_name}')

@bot.message_handler()
def info(message):
    if message.text.lower() == 'писатель':
        bot.send_message(message.chat.id,'Хемингуэй')
    elif message.text.lower() == 'поэт':
        bot.send_message(message.chat.id, 'Шекспир')
    elif message.text.lower() == 'книга':
        bot.send_message(message.chat.id, 'Три товарища')
    elif message.text.lower() == 'монолог':
        bot.send_message(message.chat.id, 'Быть или не быть')


bot.polling(none_stop=True)