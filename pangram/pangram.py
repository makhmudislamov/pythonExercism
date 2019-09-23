import string

def is_pangram(sentence):
    all_letters = string.ascii_letters
    
    # loop over the all_letters
    # check if the sentences containts all letters from all_letters
    # if yes: return true
    # else: return false

    for letter in all_letters:
        if letter in sentence:
            return True
        else:
            return False