#!usr/bin/python
#https://github.com/AngelSecurityTeam/SubForceDomain/
import threading
import time
import random
import sys
import socket
from copy import copy
import threading

if len(sys.argv) !=3:       
   print(" \033[1;35m  _____       _     ______                 _____                                  ")    
   print(" \033[1;35m / ____|     | |   |  ____|               |  __ \                      (_)        ")
   print(" \033[1;35m| (___  _   _| |__ | |__ ___  _ __ ___ ___| |  | | ___  _ __ ___   __ _ _ _ __    ")
   print(" \033[1;35m \___ \| | | | '_ \|  __/ _ \| '__/ __/ _ \ |  | |/ _ \| '_ ` _ \ / _` | | '_ \   ")
   print(" \033[1;39m ____) | |_| | |_) | | | (_) | | | (_|  __/ |__| | (_) | | | | | | (_| | | | | |  ")
   print(" \033[1;39m|_____/ \__,_|_.__/|_|  \___/|_|  \___\___|_____/ \___/|_| |_| |_|\__,_|_|_| |_|  ")
   print("                           \033[1;39m                                   |AngelSecurityTeam|  \033[1;39m ")
   
   print(" python subforcedomain.py [URL] [Wordlist]")                                                                             
   sys.exit(1)                                                                          
try:
  	palabras = open(sys.argv[2], "r").readlines()
except(IOError): 
   print("Archivo no encontrado")
   sys.exit(1)
diccionario = copy(palabras)
def cargar():
	for dic in diccionario:
		palabras.append(dic)		
def word():
	lock = threading.Lock()
	lock.acquire()
	if len(palabras) != 0:
		opcion = random.sample(palabras,  1)
		palabras.remove(opcion[0])		
	else:
		cargar()
		opcion = random.sample(palabras,  1)		
	lock.release()
	return opcion[0]

print(" \033[1;35m  _____       _     ______                 _____                                  ")    
print(" \033[1;35m / ____|     | |   |  ____|               |  __ \                      (_)        ")
print(" \033[1;35m| (___  _   _| |__ | |__ ___  _ __ ___ ___| |  | | ___  _ __ ___   __ _ _ _ __    ")
print(" \033[1;35m \___ \| | | | '_ \|  __/ _ \| '__/ __/ _ \ |  | |/ _ \| '_ ` _ \ / _` | | '_ \   ")
print(" \033[1;39m ____) | |_| | |_) | | | (_) | | | (_|  __/ |__| | (_) | | | | | | (_| | | | | |  ")
print(" \033[1;39m|_____/ \__,_|_.__/|_|  \___/|_|  \___\___|_____/ \___/|_| |_| |_|\__,_|_|_| |_|  ")
print("                           \033[1;39m                                   |AngelSecurityTeam|  \033[1;39m ")
   
print(" python subforcedomain.py [URL] [Wordlist]")

	
         		
class funcional(threading.Thread):	
	def run(self):
		opcion = word()
		try:			
			opcion1 = opcion[:-1]+"."+sys.argv[1]			
			resultado = socket.getaddrinfo(opcion1, None, 0, socket.SOCK_STREAM)
			print("\n\033[1;35m[OK]\033[1;39m",[x[4][0] for x in resultado][0],"\033[1;35m :\033[1;39m ",opcion1)
		except(socket.gaierror) as msg: 
			pass 
for i in range(len(palabras)):
	funcional1 = funcional()
	time.sleep(1)
	funcional1.start()
