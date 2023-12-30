#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
	II) Bloc B
		Each character is substituted
"""

from configs.configs_setting import key_number, len_charac_sub, charac_sub
from random import choice
import os


if os.path.exists("keylib.txt"):
	key_list = open('keylib.txt','r',encoding="utf-8").readlines()
else:
	from key_generator import key_lib_generator
	key_lib_generator(key_number[0],key_number[1])
	key_list = open('keylib.txt','r',encoding="utf-8").readlines()


def cipher(plain_text):
	
	key = choice(key_list).split(' ')
	key = [element.replace('\n','') for element in key]

	for c in range(len_charac_sub):
		plain_text = plain_text.replace(charac_sub[c],key[c])
		
	return plain_text


def decipher(coded_msg):
   
	for key in key_list:
	
		key = key.split(' ')
		key = [e.replace('\n','') for e in key]
 
		for n in range(len_charac_sub):
			coded_msg = coded_msg.replace(key[n],charac_sub[n])
	
	return coded_msg

