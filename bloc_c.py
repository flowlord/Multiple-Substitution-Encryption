#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
	II) Bloc C
		Complexifie le code après la subtitution.
"""


from configs.init import*
from random import choice,randint
from subdiv_mini import x_k,x_l


def ajout_carac_b(plain_text,x):
	"""
		Ajoute de manière aléatoire un caractère du groupe_b
		dans le code dans une position au hazard, x fois.
	"""
	plain_text = list(plain_text)
	
	for _ in range(x):
		position = randint(0,len(plain_text))
		
		plain_text.insert(position, choice(groupe_b))

	plain_text = ''.join(plain_text)
	return plain_text


def enleve_carac_b(code):
	"""
	Enlève les carcatères du groupe b
	"""
	
	new_text = ""
	for element in code:
		if element not in groupe_b:
			new_text = new_text + element  
	return new_text


def obscure(code,x):
	code = ajout_carac_b(code,x)
	code = x_k(code)

	return code


def obscure_inv(code):
	code = x_l(code)
	code = enleve_carac_b(code)

	return code






