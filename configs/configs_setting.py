#!/usr/bin/env python
# -*- coding: utf-8 -*-
# K£rn£l

from string import ascii_lowercase,ascii_uppercase, ascii_letters, digits, punctuation
import json
import os.path
from random import shuffle

def gen_default_setting():
	data = """
{
        "cipher": "ascii_letters",
        "carac_special": "easintrluodchEASINTRLUODCH0123456789!#$%&'()*+,-./:;<=>?\\"@[\\\]",
        "substitue_with": "configs/all.txt",
        "cipher_punctuation": "True",
        "cipher_accent": "True",
        "cipher_digits": "True",
        "len_caractere": [6,9],
        "len_carac_special": [3,6],
        "nombre_cle": [3,50],
        "len_carac_group_b":[4,10],
        "mini": 24,
        "maxi": 300
}
"""
	f = open("configs/setting.json", "w", encoding="utf-8")

	f.write(data)

	f.close()

if os.path.exists("configs/setting.json") is False:
	gen_default_setting()


accent = 'ÄÀÂÉÈÊËÎÏÔÙÛÜÇàâéèêëîïôùûüç'

data = json.load(open('configs/setting.json', 'r'))

carac_sub = data['cipher']

carac_special = data['carac_special']


if data['cipher'] == 'ascii_lowercase':
	carac_sub = ascii_lowercase
elif data['cipher'] == 'ascii_uppercase':
	carac_sub = ascii_uppercase
elif data['cipher'] == 'ascii_letters':
	carac_sub = ascii_letters
else:
	raise Exception('MSE ERROR: uknown cipher option')


msg_error_uknown_value = 'MSE ERROR: uknown value (only True or False)'

if data["cipher_punctuation"] == "True":
	carac_sub = carac_sub+ punctuation
elif data["cipher_punctuation"] == "False":
        pass
else:
	raise Exception(msg_error_uknown_value)

if data["cipher_digits"] == "True":
	carac_sub = carac_sub+ digits
elif data["cipher_digits"] == "False":
        pass
else:
	raise Exception(msg_error_uknown_value)

if data["cipher_accent"] == "True":
	carac_sub = carac_sub+ accent
elif data["cipher_accent"] == "False":
        pass
else:
	raise Exception(msg_error_uknown_value)


carac_sub = carac_sub+ ' '
len_carac_sub = len(carac_sub)

name = data['substitue_with']


if os.path.exists(name) is False:
	raise Exception('MSE ERROR: carac file name not found')


len_caractere = data['len_caractere']
longeur_carac_special = data['len_carac_special']
nombre_cle = data['nombre_cle']
len_carac_group_b = data["len_carac_group_b"]
min_add_group_b,max_add_group_b = data['mini'],data['maxi']


groupe_caracteres_initial = "".join(open(name,'r',encoding='utf-8').readlines())
milieu = int(len(groupe_caracteres_initial)/2)
groupe_a = groupe_caracteres_initial[:milieu]
groupe_b = groupe_caracteres_initial[milieu:]



