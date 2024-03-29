#!/usr/bin/env python
# -*- coding: utf-8 -*-
# K£rn£l

from string import ascii_lowercase,ascii_uppercase, ascii_letters, digits, punctuation
import json
import os.path

accent = "ÄÀÂÉÈÊËÎÏÔÙÛÜÇàâéèêëîïôùûüç"

data = json.load(open("configs/setting.json", "r"))

charac_sub = data["cipher"]

special_charac = data["special_charac"]
special_charac = special_charac + '"\\'


if data["cipher"] == "ascii_lowercase":
	charac_sub = ascii_lowercase
elif data["cipher"] == "ascii_uppercase":
	charac_sub = ascii_uppercase
elif data["cipher"] == "ascii_letters":
	charac_sub = ascii_letters
else:
	raise Exception("MSE ERROR: uknown cipher option")


msg_error_uknown_value = "MSE ERROR: uknown value (only True or False)"

if data["cipher_punctuation"] == "True":
	charac_sub = charac_sub+ punctuation
elif data["cipher_punctuation"] == "False":
        pass
else:
	raise Exception(msg_error_uknown_value)

if data["cipher_digits"] == "True":
	charac_sub = charac_sub+ digits
elif data["cipher_digits"] == "False":
        pass
else:
	raise Exception(msg_error_uknown_value)

if data["cipher_accent"] == "True":
	charac_sub = charac_sub+ accent
elif data["cipher_accent"] == "False":
        pass
else:
	raise Exception(msg_error_uknown_value)


charac_sub = charac_sub+ " "
len_charac_sub = len(charac_sub)
name = data["substitue_with"]


if os.path.exists(name) is False:
	raise Exception("MSE ERROR: charac file name not found")


charac_len = data["charac_len"]
len_special_charac = data["len_special_charac"]
key_number = data["key_number"]
len_charac_group_b = data["len_charac_group_b"]
mini_add_group_b_charac,maxi_add_group_b_charac = data["mini_add_group_b_charac"],data["max_add_group_b_charac"]


init_charac_group = "".join(open(name,"r",encoding="utf-8").readlines())
middle = int(len(init_charac_group)/2)
group_a = init_charac_group[:middle]
group_b = init_charac_group[middle:]




