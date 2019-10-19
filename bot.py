from telegram.ext import Updater, CommandHandler
import logging
import os, sys, re
import string
import random
import requests
from functools import partial
import time
from telegram.error import (TelegramError, Unauthorized, BadRequest, TimedOut, ChatMigrated, NetworkError)
from telegram.ext import MessageHandler, Filters

to = None

updater = Updater(token= '957266795:AAHewWLVfyyAYhHMAOPP9zukcT9AENWwrqc', use_context=True)

dispatcher = updater.dispatcher

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s' ,level=logging.INFO)

def start(update, context):

	context.bot.send_message(chat_id=update.message.chat_id, text="Thank you for using me!! \n.. press -> /toEng to translate any language to English \npress -> /toAmh to translate any language to Amharic")


def toeng(update, context, to):
	to = 'e'
	
	context.bot.send_message(chat_id=update.message.chat_id, text="I will be translating to English from now on")
	return to

def toamh(update, context, to):
	to = 'a'
	context.bot.send_message(chat_id=update.message.chat_id, text ="I will be translating to Amharic from now on..")
	return to
	
def trans(update, context, to):
	USER_AGENT = 'Chrome'
	
	if to == None:
		context.bot.send_message(chat_id=update.message.chat_id, text = "Sorry, you should first set the language to which I transelate \nUse the above commands to set!")
	elif to == 'a':
		headers = { 'User-Agent': USER_AGENT }
		kal = update.message.text
		the_kal = kal.replace(' ', '+')
		url = 'https://translate.google.com/m?hl=am&sl=auto&tl=am&ie=UTF-8&prev=_m&q={}'.format(the_kal)
		r = requests.get(url, headers = headers, proxies = {"httpl": "http://196.189.114.117:80/"})
		soup = bs(r.text, 'html.parser')
		tran = soup.find(class_='t0').contents[0]
		context.bot.send_message(chat_id = update.message.chat_id, text = tran)
		
	elif to == 'e':
		
		headers = { 'User-Agent': USER_AGENT }
		kal = update.message.text
		the_kal = kal.replace(' ', '+')
		url = 'https://translate.google.com/m?hl=am&sl=auto&tl=en&ie=UTF-8&prev=_m&q=mi+amor{}'.format(the_kal)
		r = requests.get(url, headers = headers, proxies = {"httpl": "http://196.189.114.117:80/"})
		soup = bs(r.text, 'html.parser')
		tran = soup.find(class_='t0').contents[0]
		context.bot.send_message(chat_id = update.message.chat_id, text = tran)

toeng_handler = CommandHandler('toEng', toeng)

dispatcher.add_handler(toeng_handler)

toamh_handler = CommandHandler('toAmh', toamh)

dispatcher.add_handler(toamh_handler)

start_handler = CommandHandler('start', start)

dispatcher.add_handler(start_handler)

updater.start_polling()


