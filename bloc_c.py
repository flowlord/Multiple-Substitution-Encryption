#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
	III) Bloc C
		Complexes the code after substitution
"""


from configs.configs_setting import*
from random import choice,randint


def get_random_charac_group_b():
	mini, maxi = len_charac_group_b[0],len_charac_group_b[1]
	charac_group = ""

	for _ in range(mini,maxi):
		charac_group = charac_group + choice(group_b)
		
	return charac_group


def combine_charac_a(string_a, string_b):
    """
    	example:
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


def combine_charac_b(string_a):
    """
        example:
			string_a = ABC
			string_b = get_random_charac_group_b()
			---> AXXBXCXXXXX
    """
    
    string_b = get_random_charac_group_b()
    string_c = ""
    min_len = min(len(string_a), len(string_b))

    for i in range(min_len):
        string_c += string_a[i] + string_b[i]

    if len(string_a) > len(string_b):
        string_c += string_a[min_len:]
    elif len(string_b) > len(string_a):
        string_c += string_b[min_len:]

    return string_c


def combine_charac_c(plain_text,x):
	"""
		Randomly adds a character from group_b
		character in the code in a random position, x times.
	"""
	plain_text = list(plain_text)
	
	for _ in range(x):
		position = randint(0,len(plain_text))
		
		plain_text.insert(position, get_random_charac_group_b())

	plain_text = ''.join(plain_text)
      
	return plain_text


def obscur(string):
	"""
		Passes text over 3 algorithms
	"""
	string = combine_charac_a(string,get_random_charac_group_b())
	string = combine_charac_b(string)
	string = combine_charac_c(string,randint(mini_add_group_b_charac,mini_add_group_b_charac))

	return string


def remove_group_charac_b(code):
	"""
		Remove characters from group b
	"""
	
	new_text = ""
	for element in code:
		if element not in group_b:
			new_text = new_text + element  
	return new_text



