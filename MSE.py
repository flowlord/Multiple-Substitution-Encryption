#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
# Copyright 2019-2023 by Detrox922. All Rights Reserved.
#
# Permission to use, copy, modify, and distribute this software and its
# documentation for any purpose and without fee is hereby granted,
# provided that the above copyright notice appear in all copies and that
# both that copyright notice and this permission notice appear in
# supporting documentation, and that the name of Detrox922
# not be used in advertising or publicity pertaining to distribution
# of the software without specific, written prior permission.
# Detrox922 DISCLAIMS ALL WARRANTIES WITH REGARD TO THIS SOFTWARE, INCLUDING
# ALL IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL
# Detrox922 BE LIABLE FOR ANY SPECIAL, INDIRECT OR CONSEQUENTIAL DAMAGES OR
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

	Enigma Creation Engine

	Créer le mardi 22 janvier 2019 à 01:10 

"""

__author__  = "Detrox922"
__version__ = "26.4.0"
__date__    = "28 septembre 2023"


from random import randint
from pyperclip import copy

from bloc_a import complexifier,complexifier_inv
from bloc_b import cipher,decipher
from bloc_c import ajout_carac_b,enleve_carac_b

from configs.confing_setting import*


def mse_cipher(msg,auto_copy=True):
	"""
	MESSAGE --> |A| --> |B| -->|C| --> CODED MESSAGE
	"""
	a  = complexifier(msg)
	b = cipher(a)
	c = ajout_carac_b(b,)
	
	if auto_copy is True:
		copy(c)
	return c


def mse_decipher(msg, auto_copy=False):
	"""
	CODED MESSAGE --> |C| --> |B| --> |A| --> MESSAGE
	"""
	
	c = decipher(msg)
	b = enleve_carac_b(c)
	a  = complexifier_inv(b)

	if auto_copy is True:
		copy(a)
	
	return a




message = mse_cipher("hello fish")
print(mse_decipher(message))

