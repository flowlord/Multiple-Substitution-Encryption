#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
	I) Bloc A
		Série d'opération sur une chaine de caractère
		servant à modifier le texte entré.
"""

from text_obscur import process_sentence


def complexify(plain_text):

	plain_text =  plain_text[::-1]
	plain_text = process_sentence(plain_text,True)

	return plain_text


def decomplexify(coded_text):

	coded_text = process_sentence(coded_text,False)
	coded_text =  coded_text[::-1]

	return coded_text



