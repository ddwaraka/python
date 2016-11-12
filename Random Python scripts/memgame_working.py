import os
global topic
topic = []
right=0

def new_game():
    print "Welcome to Memory Game! The rules are simple"
    print "You start by entering two words one by one and then before entering"
    print "the third one, you must enter the previous 2 and the cycle continues."
    print "Lets see how far you go before you forget!"
    global topic
    topic = []
    print "\nThe list is empty now"
    print "Enter first item"
    item1 = raw_input()
    item1 = item1.lower()
    topic.append(item1)
    print "List has %d items now" %len(topic)
    #print topic
    print "The game begins now\n"

    nextitem()


def nextitem():
    #os.system('cls')
    #print topic
    print "\nEnter next item"
    nex = raw_input()
    #print topic
    nex=nex.lower()
    topic.append(nex)
    #print topic
    os.system('cls')
    itemcheck()


def itemcheck():
    for i in range(0,len(topic)):
        print "Enter no of objects %d" %len(topic)
        
        
        #for k in reversed (range(1, len(topic)+1)):
        print "\nEnter all %d items in same order" %(len(topic)-i)
        #print i

        x=raw_input()
        x=x.lower()
        if x==topic[i]:
            print "Right"
            right = right + 1
        
        
        
        else:
            print "\nWrong Entry! Game over"
            print "You got only %d words right!" %right

            print "The right order was:"
            for i in range (0, len(topic)):
                    print topic[i]
            right = len(topic)
            if right>=0<=3:
                print "You have the most hopeless memory ever!"
            elif right>3<=8:
                print "Your memory is fairly good!"
            elif right>8<=14:
                print "Your memory is good!"
            else:
                print "Holy Shit!! Your meomory is off the charts!"


            new_game()

    nextitem()


new_game()