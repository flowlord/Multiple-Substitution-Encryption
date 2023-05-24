#!/usr/bin/env python
# -*- coding: utf-8 -*-

from random import choice
from pyperclip import paste

from MSE import mse_sha_1_cipher,mse_sha_1_decipher,mse_sha_2_cipher,mse_sha_2_decipher,mse_sha_3_cipher,mse_sha_3_decipher,mse_sha_4_cipher,mse_sha_4_decipher

from tools import rebuild,reinitialiser,mixer


exemple_phrases = ['salut agent','ceci est une longue phrase un peut chiante',
                   'meeting tonight for speak','rendez vous ce soir pour parler',
				   'hello world','on se voit ce soir','ou habitez vous',
				   'que faites vous','a bientot','a la semaine prochaine',
				   'je peux te parler','on peut se voir','jusqu ici tout va bien',
				   'mec tfk quoi la',
				   'alors la je fait expres de mettre une tres longue phrase pour des test',
				   'hallo zusammen heute','mec tfk quoi']


# Mélanger les caractères spéciaux ( avec le jeu de caractère actuelle)
#mixer()

# Reconstruit le jeu de caractère actuelle
#rebuild()

# Pour chiffrer plusieurs message et le mettre dans un fichier
#mse_cipher_file('result.txt',exemple_phrases)

# Pour déchiffrer plusieurs message dans un fichier
#mse_decipher_file('result.txt')

# Pour supprimer les clés de chiffrement
#reinitialiser()

# Chiffrer un message
#message = mse_cipher("Bonjour tous le monde")
#print(message)

# Déchiffrer
#print(mse_decipher(message))


msg = "hello world"


# Chiffrement / déchiffrement MSE SHA 1

print("MSE SHA 1")
m1 = mse_sha_1_cipher(msg)
print(m1)
print(mse_sha_1_decipher(m1))
print("\n\n\n")


# Chiffrement / déchiffrement MSE SHA 2

print("MSE SHA 2")
m2 = mse_sha_2_cipher(msg)
print(m2)
print(mse_sha_2_decipher(m2))
print("\n\n\n")

# Chiffrement / déchiffrement MSE SHA 3

print("MSE SHA 3")
m3 = mse_sha_3_cipher(msg)
print(m3)
print(mse_sha_3_decipher(m3))
print("\n\n\n")

# Chiffrement / déchiffrement MSE SHA 4

print("MSE SHA 4")
m4 = mse_sha_4_cipher(msg)
print(m4)
print(mse_sha_4_decipher(m4))
print("\n\n\n")





