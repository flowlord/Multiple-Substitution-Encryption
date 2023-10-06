#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
	II) Bloc C
		Complexifie le code après la subtitution.
"""


from configs.confing_setting import*
from random import choice,randint


def get_rand_carac_b():
	return choice(groupe_b)


def get_rand_groupe_carac_b(mini,maxi):
	group_carac = ""

	for _ in range(mini,maxi):
		group_carac = group_carac + get_rand_carac_b()
	
	return group_carac


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


def combiner_chaines_a(string_a, string_b):
    string_c = ""
    min_len = min(len(string_a), len(string_b))

    for i in range(min_len):
        string_c += string_a[i] + string_b[i]

    if len(string_a) > len(string_b):
        string_c += string_a[min_len:]
    elif len(string_b) > len(string_a):
        string_c += string_b[min_len:]

    return string_c


def combiner_chaines_b(string_a):
    mini, maxi = 2,50
    
    string_b = get_rand_groupe_carac_b(mini, maxi)
    string_c = ""
    min_len = min(len(string_a), len(string_b))

    for i in range(min_len):
        string_c += string_a[i] + string_b[i]

    if len(string_a) > len(string_b):
        string_c += string_a[min_len:]
    elif len(string_b) > len(string_a):
        string_c += string_b[min_len:]

    return string_c


def combiner_chaines_c(string_a,x):

	for e in range(x):
		
		string_b = get_rand_groupe_carac_b(3, 100)

		# Exemples d'utilisation
		msg_a = combiner_chaines_a(string_a, string_b)

		# Exemple d'utilisation
		msg_b = combiner_chaines_b(msg_a)


	return msg_b


def at_final(string):
	string = ajout_carac_b(string,randint(min_nbr_key,max_nbr_key))
	string = combiner_chaines_c(string,)


def enleve_carac_b(code):
	"""
	Enlève les carcatères du groupe b
	"""
	
	new_text = ""
	for element in code:
		if element not in groupe_b:
			new_text = new_text + element  
	return new_text




