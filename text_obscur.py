#!/usr/bin/env python
# -*- coding: utf-8 -*-

from configs.confing_setting import rolling


def split_word(word):
    """
    Sépare le mot en fonction de sa longueur.
    """
    mid = len(word)//2

    if len(word) % 2 == 0:
        return word[mid:] , word[:mid]
    else:
        return word[mid:-1], word[:mid] + word[-1]


def reverse_word(word):
    """
    Inverse le mot selon l'algorithme donné.
    """
    first, second = split_word(word)
    return first+second


def revert_word(word):
    """
    Rétablit le mot dans son ordre original.
    """
    first, second = split_word(word)
    return first+second


def process_sentence(sentence, inverse):
    """
    Traite chaque mot dans la phrase avec la fonction fournie.
    """
    if inverse is True:
        return ' '.join([reverse_word(word) for word in sentence.split(" ")])
    else:
        return ' '.join([revert_word(word) for word in sentence.split(" ")])


