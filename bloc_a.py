#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
	I) Bloc A
		Serie d'opération sur une chaine de caractère
		servant à modifier le text entré.
"""

from text_obscur import process_sentence

def complexifier(plain_text):
	"""
		example:
			hello word ---> lrowd lleho
	"""

	plain_text =  plain_text[::-1]
	plain_text = process_sentence(plain_text,True)

	return plain_text


def complexifier_inv(coded_text):
	""" 
		Remet le text dans le bon sens
		example:
			rowdl lehol ---> hello world
	"""

	coded_text = process_sentence(coded_text,False)
	coded_text =  coded_text[::-1]

	return coded_text
