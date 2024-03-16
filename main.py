import telebot
from telebot.types import *

bot = telebot.TeleBot("TELEGRAM_BOT_TOKEN")

@bot.message_handler(commands=['start'])
def welcome(msg):
    cid = msg.chat.id
    bot.reply_to(msg,"Iltimos isim yuboring!")
    
@bot.message_handler(content_types=['text'])
def custom(msg):
    cid = msg.chat.id
    text = msg.text
    bot.send_photo(cid,f"https://itpayariq.uz/api/pic/?name={text}&action=1")
    bot.send_photo(cid,f"https://itpayariq.uz/api/pic/?name={text}&action=2")
    bot.send_photo(cid,f"https://itpayariq.uz/api/pic/?name={text}&action=3")
    bot.send_photo(cid,f"https://itpayariq.uz/api/pic/?name={text}&action=4")
    

    
print(bot.get_me())
bot.infinity_polling()

#@BolqiboyevUz
