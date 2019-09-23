
import string


def is_pangram(sentence):
    alphabet = list(string.ascii_lowercase)
    sentence = sentence.lower()
    return all((char in sentence) for char in alphabet)
