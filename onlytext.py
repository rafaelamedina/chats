#-*- coding: utf-8 -*-	

from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot
import os 
import speech_recognition as sr 


bot = ChatBot("smn")


"""conversation = [
    'Ola',
    'Ola, o que você quer fazer hoje? ',
    'Oii, o que você quer fazer hoje?',
]

trainer = ListTrainer(bot)
trainer.train(conversation)"""


while True:
    try:
        
        bot_input = bot.get_response(input())
        print('Bob:', bot_input)

    except(KeyboardInterrupt, EOFError, SystemExit):
        break
