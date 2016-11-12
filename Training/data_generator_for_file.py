import random
import string


if __name__ == "__main__":
    with open("input2.txt", 'w') as output_file:
        for i in range(1000):
            output_file.write("{},{}\n".format("".join(random.choice(string.lowercase) for i in range(5)),random.randrange(1,110)))




#FOR MY PRACTICE ONLY#

#lines = open("input.txt").readlines()

#name = raw_input("Enter a name: ")
    
#for line in lines:
    #words = line.split(",")
    
    #if words[0]==name:
        #print words[1]
        #break
    
#else:    
    #print "Not found"
    




#List Searching
list_random = ['hi','hello','hey']

#name = raw_input("enter a name: ")

#for item in list_random:
    #if name==item:
        #print "Found"
        #break
#else:    
    #print "Not found"




#MY OLD CODE - NOT REFACTORED
#import random
#import string


#def random_word(length):
    #random_chars = []
    #for i in range(length):
        #random_chars.append(random.choice(string.lowercase))
        
    #return "".join(random_chars)


#if __name__ == "__main__":
    #with open("input2.txt", 'w') as output_file:
        #for i in range(1000):
            #output_file.write(random_word(5) + "," + str(random.randrange(11, 90)) + "\n")
            #output_file.write("{},{}\n".format(random_word(5), random.randrange(11, 90)))
                  