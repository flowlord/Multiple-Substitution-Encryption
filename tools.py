#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from random import shuffle, randint
import shutil
from configs.configs_setting import name,charac_sub
from settings_generator import get_random_setting
from hashlib import sha3_512
from colorama import Fore, Style


def reset():

	if os.path.exists("keylib.txt"):
		os.remove("keylib.txt")
	
	if os.path.exists("user.data"):
		os.remove("user.data")
	
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


def mixer():
	"""
		example:
			AAAZZZ ---> | mixer | ---> ZAAZAZ
	"""
	reset()
	
	init = open(name,"r",encoding="utf-8").readlines()
	init = "".join(init)
	init = list(init)

	shuffle(init)

	res = "".join(init)

	f = open(name,"w",encoding="utf-8")
	f.write(res)
	f.close()


def rebuild():
	"""
		Rebuilds the special characters file (substitue_with setting)
		deleting duplicates and also the characters
		indicated in charac_sub
	"""
	reset()
	
	old_carac = open(name,"r",encoding="utf-8").read()
	new_carac = []
	
	for e in old_carac:
		if e not in charac_sub and e not in new_carac:
			if e != "\n":
				new_carac.append(e)
	
	new_carac = "".join(new_carac)
	
	open(name,"w",encoding="utf-8").write(new_carac)


def gen_db_text(name, lenght=3000):
    """
    	Generates a new text database
		example: gen_db_text("configs/light_weight",500)
    """
    rg = open("configs/all.txt", "r", encoding="utf-8").read()

    new_data = rg[0:lenght]
    open("configs/"+name, "w", encoding="utf-8").write(new_data)


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


def first_mixer():
	"""
		Mixes character order and generates random parameters,
		if the user is using the program for the first time.
	"""

	if os.path.exists("user.txt") is False:

		db = "all.txt"

		get_random_setting(db)
		
		gen_db_text(db, randint(250,len(open("configs/all.txt", "r", encoding="utf-8").read())))
		mixer()
		rebuild()

		mse_version_hash = get_mse_hash()

		print(Fore.RED + f"MSE version hash: {mse_version_hash}")
		print(Style.RESET_ALL)

		f = open("user.txt", "w")
		f.write(mse_version_hash)
		f.close()

first_mixer()
