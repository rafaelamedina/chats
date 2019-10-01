"""importa todos as bibliotecas de dependência"""
from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot
import os 
import speech_recognition as sr 
import pyttsx3

#define um speaker como pyttsx3.init(), utilizado para a síntese de voz
speaker = pyttsx3.init()
#define o chatbot como smn (senhor meia noite), aplica um adaptador lógico, onde o bob irá responder algo padrão quando não souber o que dizer
bot = ChatBot(
'smn', 
storage_adapter='chatterbot.storage.SQLStorageAdapter',
    logic_adapters=[
        {
            'import_path': 'chatterbot.logic.BestMatch',
            'default_response': 'Hmmm... depois te respondo!',
            'maximum_similarity_threshold': 0.90
        }
    ]
)

#Treinador do bot, está comentado pois sua utilidade é apenas o treinamento de novas palavras para o bot. No exemplo de conversação, é um início de diálogo
"""conversation = [
    
]



trainer = ListTrainer(bot)
trainer.train(conversation)"""


"""while True:
message = input('Tu: ')
if message.strip() != 'Tchau Tchau':
reply=bot.get_response(message)
print('ChatBot:',reply)
if message.strip() == 'Tchau Tchau':
print('ChatBot : Tchau!')
break"""
#teste de chat, ainda não funcional
#define um leitor de texto
def speak(text):
    speaker.say(text)
    speaker.runAndWait()
	
#define a variável de reconhecimento de voz como r
r = sr.Recognizer()
#define o microfone como fonte e pede para ele ajustar para escutar o som ambiente
with sr.Microphone() as source: 
    r.adjust_for_ambient_noise(source)
    #enquanto tiver áudio: irá captar o som da fonte, reconhecer como áudio em pt
    while True:
	try:
        audio = r.listen(source)

        speech = r.recognize_google(audio, language='pt')
        #imprime você e captura a resposta
        print('Você:', speech)
	#define a variável resposta como get_response do bot, que pega o que foi falado no mic e manda para o bot analisar e voltar um resultado
        resposta = bot.get_response(speech)
	#imprime o que o bob disse
        print('Bob:', resposta)
        speak(resposta)
	#fala o que o bob disse
	except(KeybordInterrupt):
		break
