#!/usr/bin/env python
# -*- coding: utf-8 -*-

from random import choice
from pyperclip import paste

from MSE import mse_cipher,mse_decipher

from tools import rebuild,reinitialiser,mixer, gen_db_text


exemple_phrases = ['salut agent','ceci est une longue phrase un peut chiante',
                   'meeting tonight for speak','rendez vous ce soir pour parler',
				   'hello world','on se voit ce soir','ou habitez vous',
				   'que faites vous','a bientot','a la semaine prochaine',
				   'je peux te parler','on peut se voir','jusqu ici tout va bien',
				   'mec tfk quoi la',
				   'alors la je fait expres de mettre une tres longue phrase pour des test',
				   'hallo zusammen heute','mec tfk quoi']


def demo():
	print('---------- * DEMO * ----------\n')
	print('Text chiffré:\n')
	message = mse_cipher(choice(exemple_phrases), True)
	print(message,'\n\n')

	print('Texte déchiffré:\n')
	print(mse_decipher(message, False))


demo()


# Mélanger les caractères spéciaux ( avec le jeu de caractère actuelle)
#mixer()

# Reconstruit le jeu de caractère actuelle
#rebuild()

# Pour supprimer les clés de chiffrement
#reinitialiser()

# Chiffrer un message
#message = mse_cipher("Bonjour tous le monde")
#print(message)

# Déchiffrer
#print(mse_decipher(message))

#Génère une nouvelle database de text
#gen_db_text(name, lenght=999)


