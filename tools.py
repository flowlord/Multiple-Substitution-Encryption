#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from random import shuffle, choice, randint
import shutil
from configs.init import name,carac_sub
from generateur_parametre import get_random_setting

from hashlib import sha3_512
from colorama import Fore, Style


def reinitialiser():
	"""
	Suprime vos clés de chiffrement !
	"""
	
	if os.path.exists("keylib.keys"):
		os.remove("keylib.keys")
	
	try:
		shutil.rmtree('__pycache__')
		shutil.rmtree('configs/__pycache__')
	except FileNotFoundError:
		pass


def mixer():
	"""
	Mélange l'ordre des caractères
	example:
		AAAZZZ ---> | mixer | ---> ZAAZAZ
	"""
	reinitialiser()
	
	init = open(name,'r',encoding='utf-8').readlines()
	init = "".join(init)
	init = list(init)

	shuffle(init)

	res = "".join(init)

	f = open(name,'w',encoding='utf-8')
	f.write(res)
	f.close()


def rebuild():
	"""
	reconstruit le fichier des caractères spéciaux
	en supriment les doublons et aussi les caractères
	indiqués dans carac_sub
	"""
	reinitialiser()
	
	old_carac = open(name,'r',encoding='utf-8').read()
	new_carac = []
	
	for e in old_carac:
		if e not in carac_sub and e not in new_carac:
			if e != "\n":
				new_carac.append(e)
	
	new_carac = "".join(new_carac)
	
	open(name,'w',encoding='utf-8').write(new_carac)


def gen_db_text(name, lenght=999):
    """
    Génère une nouvelle database de text
	exemple: gen_db_text("configs/light_weight",500)
    """
    rg = open("configs/all.txt", "r", encoding="utf-8").read()

    new_data = rg[0:lenght]
    new_db = open("configs/"+name, "w", encoding="utf-8").write(new_data)


def get_mse_hash():
	all_files_data = b""
	for root, _, files in os.walk(os.path.dirname(__file__)):
		for filename in files:
			all_files_data = all_files_data + open(os.path.join(root, filename), "rb").read()


	return sha3_512(all_files_data).hexdigest()


def first_mixer(random_settings=False):
	"""
	Mélange l'ordre des caractères et génère des paramètre aléatoire, si
	l'utilisateur utilise pour la première fois
	le programme.
	"""

	if os.path.exists("user.data") is False:

		db = choice(["light_weight.txt", "ultra_light_weight.txt"])

		f = open("user.data", "w")
		f.close()

		if random_settings is True:
			get_random_setting(db)
		
		gen_db_text(db, randint(150,len(open("configs/all.txt", "r", encoding="utf-8").read())))
		mixer()
		rebuild()

		print(Fore.RED + f"mse version hash: {get_mse_hash()}")
		print(Style.RESET_ALL)





first_mixer(True)




