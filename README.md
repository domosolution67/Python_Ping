Programme permettant de faire des ping vers une machine, de lancer des commandes lorsque le pi est ok, de lancer des commandes lorsque le ping est NOK, lancer des commandes lorsque le ping est à nouveau OK

1 - Importation du code sur la pi :

sudo apt-get install git

sudo git clone https://github.com/domosolution67/Python_Ping /home/pi/Python_Ping

2 - Modification du code pour intergrer vos paramètres :

cd Python_Ping

nano ping.py

Paramètre pouvant être modifier :

hostname #Adresse de la machine sur laquel faire un ping, peut être une ip ou un nom de domaine

temps #Duree en seconde entre chaque ping

#Mettre les commandes si ping nok

#Mettre les commandes si ping est revenu ok
