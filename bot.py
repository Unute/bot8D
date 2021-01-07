import telebot
from datetime import datetime
from telebot import types
import random

bot = telebot.TeleBot('1545334820:AAG-tkGJ3YJPC3vn8tFzD7Qw89Hkoatdtg0');
	
keyboard1 = telebot.types.ReplyKeyboardMarkup(True)		#клавиатура
keyboard1.row('/help', '/start','🎲 Рандомное число','😊 Как дела?')

@bot.message_handler(commands=['start']) 	#приветствие
def start_message(message):
	bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAKhpl_0oXpwim4GYj9kneTXMKCCmRLOAAIBAAOSnx4RCl9TAuwX5vYeBA')
	 
	bot.send_message(message.chat.id, 'Привет, {0.first_name}. \nНапиши /help что бы узнать мой функционал\nP.S. Добавляются новые функции, перед каждым использованием писать "/start"'.format(message.from_user, bot.get_me()),
	reply_markup=keyboard1)


@bot.message_handler(content_types=['text','document', 'audio'])
def send_text(message):
	if message.chat.type == 'private':
		if message.text == "🎲 Рандомное число":
				bot.send_message(message.chat.id, str(random.randint(0,100)))
		elif message.text == '😊 Как дела?':
	 
			markup = types.InlineKeyboardMarkup(row_width=2)
			item1 = types.InlineKeyboardButton("Как джип нисcан", callback_data='good')
			item2 = types.InlineKeyboardButton("Хорошо...", callback_data='bad')
				 
			markup.add(item1, item2)
				 
			bot.send_message(message.chat.id, 'Отлично, как сам?', reply_markup=markup)
		elif message.text.lower() == 'пока':
			bot.send_message(message.chat.id, 'Прощай')
		elif message.text.lower() == 'я спать':
			bot.send_message(message.chat.id, 'Спокойной ночи')
		elif message.text.lower() == 'что делаешь' or message.text.lower() == 'что делаешь?':
			bot.send_message(message.chat.id, 'Прогресирую')
		elif message.text.lower() == '/help':
			bot.send_message(message.chat.id, 'Это 1-ый и учебный бот \nДобавлены функции:\nПривет\nПока\nЯ спать\nКак дела?\nЧто делаешь?\n🎲 Рандомное число\n\n\n\nИлья лох\n')
		else:
			bot.send_message(message.chat.id,'попробуй написать другой запрос или посмотри что я могу с помощью команды /help')


@bot.callback_query_handler(func=lambda call:True)
def callback_inline(call):
	try:
		if call.message:
			if call.data == 'good':
				bot.send_message(call.message.chat.id, '-')
			elif call.data == 'bad':
				bot.send_message(call.message.chat.id, 'Бывает 😢')

				#удаление кнопок
				bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="😊 Как дела?",
					reply_markup=None)
	
	except Exception as e:
		print(repr(e))

@bot.message_handler(content_types=['photo'])
def text_handler(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, 'Красиво.')
		
	
		
bot.polling(none_stop=True)