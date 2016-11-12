#This program was written to help me understand the random_word function
#used in data_gen_for_excel better. 

import random
import string

#This is what that program does in one line
def random_word(length):
    random_chars = []
    for i in range(length):
        random_letter = random.choice(string.lowercase)
        print random_letter, type(random_letter)
        random_chars.append(random_letter)
        
    return "".join(random_chars)
    


if __name__ == "__main__":
    print random_word(5)