#!/usr/bin/env python
# -*- coding: utf-8 -*-

def split_word(word):

    middle = len(word)//2

    if len(word) % 2 == 0:
        return word[middle:] , word[:middle]
    else:
        return word[middle:-1], word[:middle] + word[-1]


def reverse_word(word):
    first, second = split_word(word)
    return first+second


def revert_word(word):
    first, second = split_word(word)
    return first+second


def process_sentence(sentence, inverse):
    """
        process each word in the sentence with the function provided
    """

    if inverse is True:
        return " ".join([reverse_word(word) for word in sentence.split(" ")])
    
    else:
        return " ".join([revert_word(word) for word in sentence.split(" ")])

