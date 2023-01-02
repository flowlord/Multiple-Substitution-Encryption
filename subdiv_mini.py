#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
SUBDIV MINI
-----------
Principe et fonctionnement

on divise le mot au milieu et met la première moitié à la fin
et si le nombre de lettres est impair,
la dernière moitié du mot reçoit le caractère supplémentaire.

Combi = Combinaision

"""
from configs.init import rolling

def milieu(char):
	"""
	abcd --> nombre de carcatères --> 4 --> 4/2 ---> 2
	"""
	return int(len(char)/2)


def Combi_impaire_1(word):
	"""
	ABCDE --> CDEAB
	"""
	m = milieu(word)
	start = word[:m]
	middle = word[m:-1]
	end = word[-1]
	return middle+end+start

def Combi_impaire_inv(word):
	"""
	CDEAB --> ABCDE
	"""
	m = milieu(word)
	start = word[m+1:]
	middle = word[:m]
	end = word[m]
	return start+middle+end


def Combi_paire(word):
	m = milieu(word)
	start = word[:m]
	end = word[m:]
	return end+start
	
def Combi_paire_inv(word):
	m = milieu(word)
	start = word[m:]
	end = word[:m]
	return start+end


def inverser_mot(word):
	n = len(word)
	
	if n == 1:
		return word
	elif n%2 == 0:
		return Combi_paire(word)
	else:
		return Combi_impaire_1(word)


def remettre_mot(word):
	n = len(word)
	
	if n == 1:
		return word
	elif n%2 == 0:
		return Combi_paire_inv(word)
	else:
		return Combi_impaire_inv(word)


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


def k_verse(text):
	text = inverser_phrase(text)
	text = inverser_mot(text)
	return text


def k_inverse(text):
	text = remettre_mot(text)
	text = remettre_phrase(text)

	return text


def x_k(text):

	for _ in range(rolling+1):
		text = k_verse(text)
	return text


def x_l(text):

	for _ in range(rolling+1):
		text = k_inverse(text)
	return text



