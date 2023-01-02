#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
# Copyright 2019-2023 by Moon Kerling. All Rights Reserved.
#
# Permission to use, copy, modify, and distribute this software and its
# documentation for any purpose and without fee is hereby granted,
# provided that the above copyright notice appear in all copies and that
# both that copyright notice and this permission notice appear in
# supporting documentation, and that the name of Moon Kerling
# not be used in advertising or publicity pertaining to distribution
# of the software without specific, written prior permission.
# Moon Kerling DISCLAIMS ALL WARRANTIES WITH REGARD TO THIS SOFTWARE, INCLUDING
# ALL IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL
# Moon Kerling BE LIABLE FOR ANY SPECIAL, INDIRECT OR CONSEQUENTIAL DAMAGES OR
# ANY DAMAGES WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER
# IN AN ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT
# OF OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.


	███╗   ███╗  ██████╗ ███████╗
	████╗ ████║ ██╔════╝ ██╔════╝
	██╔████╔██║ ╚█████╗  █████╗
	██║╚██╔╝██║  ╚═══██╗ ██╔══╝
	██║ ╚═╝ ██║ ██████╔╝ ███████╗
	╚═╝     ╚═╝ ╚═════╝  ╚══════╝
	
	MSE (multiple substitution encryption)

	Créer le mardi 22 janvier 2019 à 01:10 

"""

__author__  = "Moon Kerling"
__version__ = "17.1.0"
__date__    = "2 janvier 2022"

from random import randint
from pyperclip import copy

from bloc_a import complexifier,complexifier_inv
from bloc_b import cipher,decipher
from bloc_c import obscure,obscure_inv

from configs.init import*


def mse_cipher(msg):
	"""
	|A| --> |B| --> |C|
	"""
	a  = complexifier(msg)
	b = cipher(a)
	c = obscure(b,randint(mini,maxi))
	
	copy(c)
	return c


def mse_decipher(msg):
	"""
	|C| --> |B| --> |A|
	"""
	c = obscure_inv(msg)
	b = decipher(c)
	a = complexifier_inv(b)
	
	return a


def mse_cipher_file(filename,list):

	file = open(filename,'w',encoding="utf-8")

	for e in list:
		file.write(mse_cipher(e))
		file.write('\n\n')

	file.close()


def mse_decipher_file(filename):

	file = open(filename,'r',encoding="utf-8").read()

	file = file.split('\n\n')

	for line in file:
		print(mse_decipher(line))




