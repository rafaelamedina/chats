"""importa o reconhecimento de voz"""

import speech_recognition as sr 

r = sr.Recognizer() 

""" define a variável para reconhecimento de voz"""

with sr.Microphone() as source 
"""identifica o mic como fonte""" 
	r.adjust_for_ambient_noise(source) 
	""" Ajusta o mic para reconhecer a voz ambiente"""
	while True: 
		audio = r.listen(source)
		"""escuta da fonte source"""
		speech = r.recognize_google(audio, language='pt' )
		
		print('Você disse isso aqui o seu coco: ', speech)
		"""imprime o que o usuário disse"""	
		
