import telebot
from datetime import datetime
from telebot import types

bot = telebot.TeleBot('1545334820:AAG-tkGJ3YJPC3vn8tFzD7Qw89Hkoatdtg0')

keyboard1 = telebot.types.ReplyKeyboardMarkup(True)		#клавиатура
keyboard1.row('/start', 'Записать Д/З', 'Узнать Д/З')

RUS = []        #Русский язык
ALG = []		#Алгебра
LIT = []		#Литература
BIO = []		#Биология
IST = []		#История
GEO = []		#География
GMT = []		#Геометрия
HIM = []		#Химия
OBSHEST = []	#Обществознание
RODN_RUS = []   #Родной язык
PHY = []		#Физика
MUS = []		#Музыка
ISO = []		#Изо
INFORM = []		#Информатика
OBZH = []		#ОБЖ
SK_MAT = []		#СК(математика)
TECHNOLOGY = []	#Технология
ENGLISH_1 = []	#Англ.яз(группа Люсине Самвеловны)
ENGLISH_2 = []	#Англ.яз (группа Марины Николаевны)

@bot.message_handler(commands=['start']) 	#приветствие
def start_message(message):	 
	bot.send_message(message.chat.id, 'Привет, {0.first_name}. Здесь можно узнавать и записывать Д/З'.format(message.from_user, bot.get_me()),
	reply_markup=keyboard1)


@bot.message_handler(content_types=['text','document', 'audio'])
def send_text(message):
	if message.text == 'Записать Д/З':
		
		markup = types.InlineKeyboardMarkup(row_width=2)
		
		item1 = types.InlineKeyboardButton("Русский язык", callback_data='RUS_')
		item2 = types.InlineKeyboardButton("Алгебра", callback_data='ALG_')
		item3 = types.InlineKeyboardButton("Литература", callback_data='LIT_')
		item4 = types.InlineKeyboardButton("Биология", callback_data='BIO_')
		item5 = types.InlineKeyboardButton("История", callback_data='IST_')
		item6 = types.InlineKeyboardButton("География", callback_data='GEO_')
		item7 = types.InlineKeyboardButton("Геометрия", callback_data='GMT_')
		item8 = types.InlineKeyboardButton("Химия", callback_data='HIM_')
		item9 = types.InlineKeyboardButton("Обществознание", callback_data='OBSHEST_')
		item10 = types.InlineKeyboardButton("Родной язык", callback_data='RODN_RUS_')
		item11 = types.InlineKeyboardButton("Физика", callback_data='PHY_')
		item12 = types.InlineKeyboardButton("Музыка", callback_data='MUS_')
		item13 = types.InlineKeyboardButton("Изо", callback_data='ISO_')
		item14 = types.InlineKeyboardButton("Информатика", callback_data='INFORM_')
		item15 = types.InlineKeyboardButton("ОБЖ", callback_data='OBZH_')
		item16 = types.InlineKeyboardButton("СК(математика)", callback_data='SK_MAT_')
		item17 = types.InlineKeyboardButton("Технология", callback_data='TECHNOLOGY_')
		item18 = types.InlineKeyboardButton("Англ.яз(группа Люсине Самвеловны)", callback_data='ENGLISH_1_')
		item19 = types.InlineKeyboardButton("Англ.яз (группа Марины Николаевны)", callback_data='ENGLISH_2_')
		
		markup.add(item1, item2, item3, item4, item5, item6, item7, item8, item9, item10, item11, item12, item13, item14, item15, item17, item18, item19)
		
		bot.send_message(message.chat.id, 'На какой урок ты хочешь записать ДЗ?', reply_markup=markup)

	elif  message.text == 'Узнать Д/З':
		markup = types.InlineKeyboardMarkup(row_width=2)
		
		item1 = types.InlineKeyboardButton("Русский язык", callback_data='RUS_know')
		item2 = types.InlineKeyboardButton("Алгебра", callback_data='ALG_know')
		item3 = types.InlineKeyboardButton("Литература", callback_data='LIT_know')
		item4 = types.InlineKeyboardButton("Биология", callback_data='BIO_know')
		item5 = types.InlineKeyboardButton("История", callback_data='IST_know')
		item6 = types.InlineKeyboardButton("География", callback_data='GEO_know')
		item7 = types.InlineKeyboardButton("Геометрия", callback_data='GMT_know')
		item8 = types.InlineKeyboardButton("Химия", callback_data='HIM_know')
		item9 = types.InlineKeyboardButton("Обществознание", callback_data='OBSHEST_know')
		item10 = types.InlineKeyboardButton("Родной язык", callback_data='RODN_RUS_know')
		item11 = types.InlineKeyboardButton("Физика", callback_data='PHY_know')
		item12 = types.InlineKeyboardButton("Музыка", callback_data='MUS_know')
		item13 = types.InlineKeyboardButton("Изо", callback_data='ISO_know')
		item14 = types.InlineKeyboardButton("Информатика", callback_data='INFORM_know')
		item15 = types.InlineKeyboardButton("ОБЖ", callback_data='OBZH_know')
		item16 = types.InlineKeyboardButton("СК(математика)", callback_data='SK_MAT_know')
		item17 = types.InlineKeyboardButton("Технология", callback_data='TECHNOLOGY_know')
		item18 = types.InlineKeyboardButton("Англ.яз(группа Люсине Самвеловны)", callback_data='ENGLISH_1_know')
		item19 = types.InlineKeyboardButton("Англ.яз (группа Марины Николаевны)", callback_data='ENGLISH_2_know')
		
		markup.add(item1, item2, item3, item4, item5, item6, item7, item8, item9, item10, item11, item12, item13, item14, item15, item17, item18, item19)

		bot.send_message(message.chat.id, 'Домашнее задание какого урока ты хочешь узнать?', reply_markup=markup)


@bot.callback_query_handler(func=lambda call:True)
def callback_inline(call):
	try:
		if call.message:
			if call.data == 'RUS_':
				bot.send_message(call.message.chat.id, 'Запиши домашнее задание', reply_markup=None)
				bot.register_next_step_handler(call.message, russkiy)
			elif call.data == 'ALG_':
				bot.send_message(call.message.chat.id, 'Запиши домашнее задание')
				bot.register_next_step_handler(call.message, algebra)
			elif call.data == 'LIT_':
				bot.send_message(call.message.chat.id, 'Запиши домашнее задание')
				bot.register_next_step_handler(call.message, litra)
			elif call.data == 'BIO_':
				bot.send_message(call.message.chat.id, 'Запиши домашнее задание')
				bot.register_next_step_handler(call.message, biology)
			elif call.data == 'IST_':
				bot.send_message(call.message.chat.id, 'Запиши домашнее задание')
				bot.register_next_step_handler(call.message, istoria)
			elif call.data == 'GEO_':
				bot.send_message(call.message.chat.id, 'Запиши домашнее задание')
				bot.register_next_step_handler(call.message, georaphy)
			elif call.data == 'GMT_':
				bot.send_message(call.message.chat.id, 'Запиши домашнее задание')
				bot.register_next_step_handler(call.message, geometry)
			elif call.data == 'HIM_':
				bot.send_message(call.message.chat.id, 'Запиши домашнее задание')
				bot.register_next_step_handler(call.message, himia)
			elif call.data == 'OBSHEST_':
				bot.send_message(call.message.chat.id, 'Запиши домашнее задание')
				bot.register_next_step_handler(call.message, obshestvoznanie)
			elif call.data == 'RODN_RUS_':
				bot.send_message(call.message.chat.id, 'Запиши домашнее задание')
				bot.register_next_step_handler(call.message, rodn_rus)
			elif call.data == 'PHY_':
				bot.send_message(call.message.chat.id, 'Запиши домашнее задание')
				bot.register_next_step_handler(call.message, physic)
			elif call.data == 'MUS_':
				bot.send_message(call.message.chat.id, 'Запиши домашнее задание')
				bot.register_next_step_handler(call.message, music)
			elif call.data == 'ISO_':
				bot.send_message(call.message.chat.id, 'Запиши домашнее задание')
				bot.register_next_step_handler(call.message, iso)
			elif call.data == 'INFORM_':
				bot.send_message(call.message.chat.id, 'Запиши домашнее задание')
				bot.register_next_step_handler(call.message, informatica)
			elif call.data == 'OBZH_':
				bot.send_message(call.message.chat.id, 'Запиши домашнее задание')
				bot.register_next_step_handler(call.message, obzh)
			elif call.data == 'SK_MAT_':
				bot.send_message(call.message.chat.id, 'Запиши домашнее задание')
				bot.register_next_step_handler(call.message, sk_mat)
			elif call.data == 'TECHNOLOGY_':
				bot.send_message(call.message.chat.id, 'Запиши домашнее задание')
				bot.register_next_step_handler(call.message, TECHNOLOGY)
			elif call.data == 'ENGLISH_1_':
				bot.send_message(call.message.chat.id, 'Запиши домашнее задание')
				bot.register_next_step_handler(call.message, english_1)
			elif call.data == 'ENGLISH_2_':
				bot.send_message(call.message.chat.id, 'Запиши домашнее задание')
				bot.register_next_step_handler(call.message, english_2)


			elif call.data == 'RUS_know':
				for a in RUS:
					bot.send_message(call.message.chat.id, a)
			elif call.data == 'ALG_know':
				for a in ALG:
					bot.send_message(call.message.chat.id, a)
			elif call.data == 'LIT_know':
				for a in LIT:
					bot.send_message(call.message.chat.id, a)
			elif call.data == 'BIO_know':
				for a in BIO:
					bot.send_message(call.message.chat.id, a)
			elif call.data == 'IST_know':
				for a in IST:
					bot.send_message(call.message.chat.id, a)
			elif call.data == 'GEO_know':
				for a in GEO:
					bot.send_message(call.message.chat.id, a)
			elif call.data == 'GMT_know':
				for a in GMT:
					bot.send_message(call.message.chat.id, a)
			elif call.data == 'HIM_know':
				for a in HIM:
					bot.send_message(call.message.chat.id, a)
			elif call.data == 'OBSHEST_know':
				for a in OBSHEST:
					bot.send_message(call.message.chat.id, a)
			elif call.data == 'RODN_RUS_know':
				for a in RODN_RUS:
					bot.send_message(call.message.chat.id, a)
			elif call.data == 'PHY_know':
				for a in PHY:
					bot.send_message(call.message.chat.id, a)
			elif call.data == 'MUS_know':
				for a in MUS:
					bot.send_message(call.message.chat.id, a)
			elif call.data == 'ISO_know':
				for a in ISO:
					bot.send_message(call.message.chat.id, a)
			elif call.data == 'INFORM_know':
				for a in INFORM:
					bot.send_message(call.message.chat.id, a)
			elif call.data == 'OBZH_know':
				for a in OBZH:
					bot.send_message(call.message.chat.id, a)
			elif call.data == 'SK_MAT_know':
				for a in SK_MAT:
					bot.send_message(call.message.chat.id, a)
			elif call.data == 'TECHNOLOGY_know':
				for a in TECHNOLOGY:
					bot.send_message(call.message.chat.id, a)
			elif call.data == 'ENGLISH_1_know':
				for a in ENGLISH_1:
					bot.send_message(call.message.chat.id, a)
			elif call.data == 'ENGLISH_2_know':
				for a in ENGLISH_2:
					bot.send_message(call.message.chat.id, a)


	except Exception as e:
		print(repr(e))	
	
def russkiy(message):
	val = message.text
	RUS.append(val)
	bot.send_message(message.chat.id, 'Готово')

def algebra(message):
	val = message.text
	ALG.append(val)
	bot.send_message(message.chat.id, 'Готово')

def litra(message):
	val = message.text
	LIT.append(val)
	bot.send_message(message.chat.id, 'Готово')

def biology(message):
	val = message.text
	BIO.append(val)
	bot.send_message(message.chat.id, 'Готово')

def istoria(message):
	val = message.text
	IST.append(val)
	bot.send_message(message.chat.id, 'Готово')

def georaphy(message):
	val = message.text
	GEO.append(val)
	bot.send_message(message.chat.id, 'Готово')

def geometry(message):
	val = message.text
	GMT.append(val)
	bot.send_message(message.chat.id, 'Готово')

def himia(message):
	val = message.text
	HIM.append(val)
	bot.send_message(message.chat.id, 'Готово')

def obshestvoznanie(message):
	val = message.text
	OBSHEST.append(val)
	bot.send_message(message.chat.id, 'Готово')

def rodn_rus(message):
	val = message.text
	RODN_RUS.append(val)
	bot.send_message(message.chat.id, 'Готово')

def physic(message):
	val = message.text
	PHY.append(val)
	bot.send_message(message.chat.id, 'Готово')

def music(message):
	val = message.text
	MUS.append(val)
	bot.send_message(message.chat.id, 'Готово')

def iso(message):
	val = message.text
	ISO.append(val)
	bot.send_message(message.chat.id, 'Готово')

def informatica(message):
	val = message.text
	INFORM.append(val)
	bot.send_message(message.chat.id, 'Готово')

def obzh(message):
	val = message.text
	OBZH.append(val)
	bot.send_message(message.chat.id, 'Готово')

def sk_mat(message):
	val = message.text
	SK_MAT.append(val)
	bot.send_message(message.chat.id, 'Готово')

def TECHNOLOGY(message):
	val = message.text
	TECHNOLOGY.append(val)
	bot.send_message(message.chat.id, 'Готово')

def english_1(message):
	val = message.text
	ENGLISH_1.append(val)
	bot.send_message(message.chat.id, 'Готово')

def english_2(message):
	val = message.text
	ENGLISH_2.append(val)
	bot.send_message(message.chat.id, 'Готово')

		
bot.polling(none_stop=True)