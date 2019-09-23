import string

def is_pangram(sentence):
    all_printables = string.printable
    
    # loop over all_printables
            # if char is in sentence and all printables
            # return true
            # else:
            # false
   
    for char in all_printables:
        for char in sentence:
            if char in sentence and char in all_printables:
                return True
            else:
                return False