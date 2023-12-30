#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
# Copyright 2019-2023 by Enron Group. All Rights Reserved.
#
# Permission to use, copy, modify, and distribute this software and its
# documentation for any purpose and without fee is hereby granted,
# provided that the above copyright notice appear in all copies and that
# both that copyright notice and this permission notice appear in
# supporting documentation, and that the name of Enron Group
# not be used in advertising or publicity pertaining to distribution
# of the software without specific, written prior permission.
# Enron Group DISCLAIMS ALL WARRANTIES WITH REGARD TO THIS SOFTWARE, INCLUDING
# ALL IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL
# Enron Group BE LIABLE FOR ANY SPECIAL, INDIRECT OR CONSEQUENTIAL DAMAGES OR
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

	Game engine for puzzle creation

	Created on Tuesday, January 22nd, 2019 at 01:10

"""

__author__  = "Enron Group"
__version__ = "27.0.3"
__date__    = "29 décembre 2023"

from pyperclip import copy

from bloc_a import complexify,decomplexify
from bloc_b import cipher,decipher
from bloc_c import obscur,remove_group_charac_b


def mse_cipher(msg,auto_copy=True):

	a  = complexify(msg)
	b = cipher(a)
	c = obscur(b)
	
	if auto_copy is True:
		copy(c)
	return c


def mse_decipher(msg, auto_copy=False):

	c = remove_group_charac_b(msg)
	b = decipher(c)
	a  = decomplexify(b)

	if auto_copy is True:
		copy(a)
	
	return a


