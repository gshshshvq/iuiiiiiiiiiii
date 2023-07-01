import telebot
from telebot import types
import requests , re

token = "6074459931:AAH53z3kyGDeANmTSIS_DpJibvHEIIHD1M8"
channel = types.InlineKeyboardButton(text='قـنـاة الـبـوت',url='t.me/BOTS22i')
bot = telebot.TeleBot(token)
@bot.message_handler(commands=["start"])
def welcome(message):
	name = message.from_user.first_name
	brok = types.InlineKeyboardMarkup()
	brok.add(channel)
	bot.reply_to(message,'اهلا {} ارسل رابط لاختصاره'.format(name),reply_markup=brok)
	
@bot.message_handler(func=lambda m:True)
def shorturl(message):
	msg = message.text
	url = f'https://is.gd/create.php?format=simple&url={msg}'
	req = requests.get(url).text
	if re.search("(?P<url>https?://[^\s]+)", msg):
		bot.reply_to(message,f'تم الاختصار: \n{req}')
	else:
		bot.reply_to(message, "sorry ,This is not a link URL")
	
print('تم التشغيل')
bot.infinity_polling()