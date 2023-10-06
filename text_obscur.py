#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
text obscurcissement
-----------
Principe et fonctionnement

on divise le mot au milieu et met la première moitié à la fin
et si le nombre de lettres est impair,
la dernière moitié du mot reçoit le caractère supplémentaire.

C = Combinaision

"""

from configs.confing_setting import rolling


# obscurcissement +


def milieu(char):
	"""
	abcd --> nombre de carcatères --> 4 --> 4/2 ---> 2
	"""
	return int(len(char)/2)


def C1(t):
	m = milieu(t)
	start = t[:m]
	middle = t[m:-1]
	end = t[-1]
	return middle+end+start

def C1_inv(t):
	m = milieu(t)
	start = t[m+1:]
	middle = t[:m]
	end = t[m]
	return start+middle+end


def inverser_mot(word):
	n = len(word)
	
	if n == 1:
		return word
	elif n%2 == 0:
		return word[n//2:] + word[:n//2]
	else:
		return C1(word)


def remettre_mot(word):
	n = len(word)
	
	if n == 1:
		return word
	elif n%2 == 0:
		return word[n//2:] + word[:n//2]
	else:
		return C1_inv(word)


def remettre_phrase(code):
	code = code.split(' ')
	msg = ''
	
	for word in code:
		msg = msg + remettre_mot(word) + ' '
	
	return msg[:-1]


def inverser_phrase(msg):
	msg = msg.split(' ')
	code = ''
	
	for word in msg:
		code = code + inverser_mot(word) + ' '
	
	return code[:-1]


# obscurcissement ++

def palm_1(msg):

	for _ in range(12):
		msg = inverser_phrase(msg)
		msg = inverser_mot(msg)

	return msg


def palm_1_rev(msg):
	for _ in range(12):
		msg = remettre_mot(msg)
		msg = remettre_phrase(msg)

	return msg


def palm_2(msg):
	for _ in range(rolling):
		msg = palm_1(msg)
	return msg


def palm_2_rev(msg):
	for _ in range(rolling):
		msg = palm_1_rev(msg)
	return msg



