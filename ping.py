#!/usr/bin/python3
# -*- coding: utf-8 -*-

#Importation de modules utilise
import os
import time

#Definition des variables
hostname = "www.google.fr" #Adresse de la machine sur laquel faire un ping
temps = 60 #Duree en seconde entre chaque ping

def ping() :
	reponse = os.system("ping -c 1 " + hostname)
	if reponse == 0 :
		return 0
	else :
		return 1

def pingnok() :
	#Mettre les commandes si ping nok
	print("Ping NOK")
	while ping() != 0 :
		time.sleep(temps)
		ping()
	#Mettre les commandes si ping est revenu ok
	print("Ping OK")
	time.sleep(temps)
	programme()

def programme() :
	ping()
	if ping() == 0 :
		print("Ping OK")
		time.sleep(temps)
		programme()
	else :
		print("Ping NOK")
		pingnok()

#Programme
print("Demarrage du programme de verification du ping")
programme()
