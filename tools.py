#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from random import shuffle, choice, randint
import shutil
from configs.configs_setting import charac_sub, len_db_all
from settings_generator import get_random_setting
from hashlib import sha3_512
from colorama import Fore, Style


def reset():

	if os.path.exists("keylib.txt"):
		os.remove("keylib.txt")
	
	if os.path.exists("user.data"):
		os.remove("user.data")
	
	if os.path.exists("configs/setting.json"):
		os.remove("configs/setting.json")

	if os.path.exists("configs/light_weight.txt"):
		os.remove("configs/light_weight.txt")

	if os.path.exists("configs/ultra_light_weight.txt"):
		os.remove("configs/ultra_light_weight.txt")
	
	if os.path.exists("configs/perso.txt"):
		os.remove("configs/perso.txt")

	try:
		shutil.rmtree("__pycache__")
		shutil.rmtree("configs/__pycache__")

	except FileNotFoundError:
		pass


def mixer(db):
	"""
		example:
			AAAZZZ ---> | mixer | ---> ZAAZAZ
		USE BEFORE GENERATE KEYS !
	"""

	init = open(db,"r",encoding="utf-8").readlines()
	init = "".join(init)
	init = list(init)

	shuffle(init)

	res = "".join(init)

	f = open(db,"w",encoding="utf-8")
	f.write(res)
	f.close()


def rebuild(db):
	"""
		Rebuilds the special characters file (substitue_with setting)
		deleting duplicates and also the characters
		indicated in charac_sub
		USE BEFORE GENERATE KEYS !
	"""
	
	old_carac = open(db,"r",encoding="utf-8").read()
	new_carac = []
	
	for e in old_carac:
		if e not in charac_sub and e not in new_carac:
			if e != "\n":
				new_carac.append(e)
	
	new_carac = "".join(new_carac)
	
	open(db,"w",encoding="utf-8").write(new_carac)


def gen_db_text(name, lenght):
	"""
		Generates a new text database
		example: gen_db_text("configs/light_weight",500)
	"""
	rg = open("configs/all.txt", "r", encoding="utf-8").read()

	new_data = rg[0:lenght]

	f = open("configs/"+name, "w", encoding="utf-8")
	f.write(new_data)
	f.close()


def get_mse_hash():
	"""
		Generates the project hash
	"""
	all_files_datas = b""
	for root, _, files in os.walk(os.path.dirname(__file__)):
		for filename in files:
			if filename not in ["requirement.txt", "user.data","README.md"]:
				if "cpython" not in filename:
					all_files_datas = all_files_datas + open(os.path.join(root, filename), "rb").read()

	return sha3_512(all_files_datas).hexdigest()


def get_bd_text_len():
	r = randint(1000,len_db_all)
	db_lenght = choice([r, "small", "medium", "large"])

	if type(db_lenght) is int:
		db_len = db_lenght
		db = "perso.txt"

	elif db_lenght == "small":
		db_len = 16444
		db = "light_weight.txt"

	elif db_lenght == "medium":
		db_len = 32889
		db = "ultra_light_weight.txt"

	elif db_lenght == "large":
		db_len = len_db_all
		db = "all.txt"
	
	return  db,db_len


def first_mixer(random_settings=False):
	"""
		Mixes character order and generates random parameters,
		if the user is using the program for the first time.
	"""

	if os.path.exists("user.data") is False:

		db, db_len = get_bd_text_len()
		
		gen_db_text(db, db_len)

		if random_settings is True:
			get_random_setting(db)
		
		mixer("configs/"+db)
		rebuild("configs/"+db)

		mse_version_hash = get_mse_hash()

		print(Fore.RED + f"MSE version hash: {mse_version_hash}")
		print(Style.RESET_ALL)

		f = open("user.data", "w")
		f.write(mse_version_hash)
		f.close()

first_mixer(True)




