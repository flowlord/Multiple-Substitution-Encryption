#!/usr/bin/env python
# -*- coding: utf-8 -*-
from random import choice
from colorama import Fore, Style
from MSE import mse_cipher, mse_decipher
from tools import reset,mixer, rebuild, gen_db_text


example_sentences = ["The sign said there was road work ahead so he decided to speed up.",
				   "She couldn't understand why nobody else could see that the sky is full of cotton candy.",
				   "They looked up at the sky and saw a million stars.",
				   "He had a hidden stash underneath the floorboards in the back room of the house.",
				   "He was surprised that his immense laziness was inspirational to others.",
				   "Someone I know recently combined Maple Syrup & buttered Popcorn thinking it would taste like caramel popcorn.", "It didn't and they don't recommend anyone else do it either.",
				   "My Mum tries to be cool by saying that she likes all the same things that I do.",
				   "She had some amazing news to share but nobody to share it with."]


def demo():
	print("---------- * DEMO * ----------\n")
	
	print(Fore.RED +"Encrypted text:\n"+Style.RESET_ALL)
	message = mse_cipher(choice(example_sentences))

	print(message,"\n\n")

	print(Fore.GREEN +"Decrypted text:\n"+Style.RESET_ALL)
	print(mse_decipher(message))


demo()

#	Chiffrer un message
#message = mse_cipher("hello fish")
#print(message)

#	Déchiffrer
#print(mse_decipher(message))

#	Pour supprimer les clés de chiffrement
#reset()



