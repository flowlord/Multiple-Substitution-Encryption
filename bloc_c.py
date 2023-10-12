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


def combiner_chaines_a(string_a, string_b):
    """
    exemple:
    string_a = A C E
    string_b = 	B D F
    ---> ABCDEF
    """
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
    """
    string_a = ABC
    string_b = get_rand_groupe_carac_b()
    ---> AXXBXCXXXXX
    """
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


def combiner_chaines_c(plain_text,x):
	"""
		Ajoute de manière aléatoire un caractère du groupe_b
		dans le code dans une position au hazard, x fois.
	"""
	plain_text = list(plain_text)
	
	for _ in range(x):
		position = randint(0,len(plain_text))
		
		plain_text.insert(position, get_rand_carac_b())

	plain_text = ''.join(plain_text)
	return plain_text


def obscur(string):
	"""
	Fait passer le texte sur 3 algorithmes.
	"""
	string = combiner_chaines_a(string,get_rand_groupe_carac_b(len_carac_group_b[0],len_carac_group_b[1]))
	string = combiner_chaines_b(string)
	string = combiner_chaines_c(string,randint(min_nbr_key,max_nbr_key))

	return string


def enleve_carac_b(code):
	"""
	Enlève les carcatères du groupe b
	"""
	
	new_text = ""
	for element in code:
		if element not in groupe_b:
			new_text = new_text + element  
	return new_text



