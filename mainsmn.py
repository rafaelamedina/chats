"""importa todos as bibliotecas de dependência"""
from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot
import os 
import speech_recognition as sr 

"""define o chatbot como smn (senhor meia noite)"""
bot = ChatBot("smn")

"""Treinador do bot, está comentado pois sua utilidade é apenas o treinamento de novas palavras para o bot. No exemplo de conversação, é um início de diálogo"""
"""conversation = [
    "Olá",
    "Olá",
    "Oii",
    
]"""

"""conversation = [
    "Tudo bem?",
    "Ótimo! e você?",
    "Estou bem e você?",
]
conversation = [
    "Também?",
    "Bom ouvir isso!",
    "Que bom!",
    "Adoro ver pessoas felizes",
]




trainer = ListTrainer(bot)
trainer.train(conversation)

"""
"""while True:
message = input('Tu: ')
if message.strip() != 'Tchau Tchau':
reply=bot.get_response(message)
print('ChatBot:',reply)
if message.strip() == 'Tchau Tchau':
print('ChatBot : Tchau!')
break""" """teste de chat, ainda não funcional"""

while True:
    try:
        
        bot_input = bot.get_response(input())
        print('Bob:', bot_input)

    except(KeyboardInterrupt, EOFError, SystemExit):
        break
		
       
