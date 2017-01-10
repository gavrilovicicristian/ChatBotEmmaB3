import json
import random

_englishLetters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
_englishLettersAndSpaces = _englishLetters + _englishLetters.lower() + ' '


def open_english_dictionary():
    dictionaryFile = open('dictionary.txt')
    englishWords = {}
    for word in dictionaryFile.read().split('\n'):
        englishWords[word] = None
    dictionaryFile.close()
    return englishWords


_possibleEnglishWords = open_english_dictionary()


def number_of_words_in_english(message):
    message = message.upper()
    message = if_is_not_letter_remove(message)
    possibleWords = message.split()
    if possibleWords == []:
        return 0.0
    matches = 0
    for word in possibleWords:
        if word in _possibleEnglishWords:
            matches += 1
    return float(matches) / len(possibleWords)


def if_is_not_letter_remove(message):
    lettersOnly = []
    for symbol in message:
        if symbol in _englishLettersAndSpaces:
            lettersOnly.append(symbol)
    return ''.join(lettersOnly)


def is_english_sentence(message, wordPercentage=20, letterPercentage=85):
    wordsMatch = number_of_words_in_english(message) * 100 >= wordPercentage
    numLetters = len(if_is_not_letter_remove(message))
    messageLettersPercentage = float(numLetters) / len(message) * 100
    lettersMatch = messageLettersPercentage >= letterPercentage
    if (wordsMatch and lettersMatch):
        return True
    return False