"""importa o reconhecimento de voz e o sistema operacional"""

import speech_recognition as sr 

"""reconhece a variável R como o reconhecimento de voz"""
r = sr.Recognizer() 

"""prepara o microfone como fonte do som e printa fale algo, depois pede para a variável áudio ser escutada pelo mic"""
with sr.Microphone() as source: 
	print('Fala algo: ') 
	audio = r.listen(source)
"""tenta reconhecer o texto através da API da google na linguagem em português"""
	try:
		text = r.recognize_google(audio, language='pt')
		print("Tu disse: {}".format(text))
"""caso não entenda, imprime "Numtendi"""
	except:
		print('num tendi')
