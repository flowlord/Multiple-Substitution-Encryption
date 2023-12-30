#!/usr/bin/env python
# coding: utf-8
# G£N£SIS K£Y

"""
	key library = keylib
	file containing several encryption keys
	Takes over part of the source code of GENESIS KEY © software, which,
	in a dark era of the project was a payware ;)
"""

from random import randint,choice
from configs.configs_setting import group_a, charac_sub, charac_len, len_special_charac, special_charac, len_charac_sub

def get_random_charac(x):

	charac = ''
	for _ in range(x):
		charac = charac+choice(group_a)
	return charac


def key_gen(len_charac_sub):
	"""
		Generates a substitution key with a chosen length
		Example:

			| DXI | TUYSQ | ZEOD | UTT | UZU | FRYS | RZ | EWQ | PMZWK |
			------------------------------------------------------------
			| a   | b     | c    | d   | e	 | f	| g  | h   | i     |
		
	"""

	key = ''

	for charac in range(len_charac_sub):

		charac_len_ = randint(charac_len[0],charac_len[1])
		special_charac_ = randint(len_special_charac[0],len_special_charac[1])
				
		if charac_sub[charac] in special_charac:
			key = key + f'{get_random_charac(special_charac_)} '
		key = key + f'{get_random_charac(charac_len_)} '

	return key[:-1]
   
   
def key_lib_generator(min_nbr_key,max_nbr_key):
	"""
		Generates a key library
	"""

	file = open('keylib.txt','w',encoding='utf-8')
	
	for _ in range(min_nbr_key,max_nbr_key):
		file.write(f'{key_gen(len_charac_sub)}\n')

	file.close()

