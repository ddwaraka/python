import random
import mystuffex40

mystuff = {'apple':"IAM APPLES!"}
print mystuff['apple']

mystuffex40.apple()
print mystuffex40.tangerine
print "\n"


class Mystuff(object):
    def __init__(self):
        self.tangerine = "Some stupid string"
    
    def apple(self):
        print "Another stupid string"
        

thing = Mystuff()
thing.apple()
print thing.tangerine
print "\n"


class Character:
    def __init__(self):
        self.name="name"
        self.health=5
        self.speed=6
        self.agility=7
        print "%s's health is %d" %(self.name, self.health)
        
        
    
    def printHam(self):
        print "Ham"
    
Dilip = Character()


print(','.join(map(str, [Dilip.health, Dilip.speed, Dilip.agility])))




class Vehicle:
    def __init__(self, vehicle_type, brand, name, wheels, doors):
        self.vehicle_type = vehicle_type
        print "This vehicle is a %s" %self.vehicle_type
        self.brand=brand
        print "This vehicle's brand is %s" %self.brand
        self.name = name
        
        self.wheels=wheels
        print "This vehicle has %d wheels" %self.wheels
        self.doors=doors
        print "This vehicle has %d doors" %self.doors
    
    def getcarname(self):
        print "This vehicle's name is %s" %self.name
        




car1=Vehicle("Truck","Ford","Pickup",4,2)
print car1.getcarname()


class Human:
    def __init__(self, name, gender):
        self.name=name
        self.gender=gender
    
    def printname(self):
        print name

will = Human("William", "Male")
print will.name

sam = Human("Samuel","Male")
print sam.name

dilip=Human("Dilip", "Male")
dilip.printname



#class Character:
    #def __init__(self, name):
        #self.name = name
        #self.health=5
        #print "%s's health is %d" %(self.name,self.health)
        #self.speed=6
        #self.agility=7
        
    
    #def printHam(self):
        #print "Ham"
    
#Gollum=Character(name='Gollum')
 


#class Ph:
    #def __init__(self):
        #self.x=5
        
    
    #def simpleinterest(self):
        #p=11
        #t=12
        #r=23
        #return p



#y=Ph()
#print y.simpleinterest()

#print y.printham


class BaseClass():
    def printham(self):
        print "Fuck Yeah"
    
class InheritClass(BaseClass):
    pass

x=InheritClass()
x.printham()


class Character(object):
    def __init__(self):
        self.health=100
        
class Blacksmith(Character):
    def __init__(self):
        super(Blacksmith, self).__init__()
    pass


bs = Blacksmith()
print bs.health



class Students(object):
    def __init__(self,):
        self.name
        self.rn=rn
        self.marks=marks
        self.std = std
        self.sports=sports
        


#Empty Object
class Object(object):
    pass

a = Object()
a.name = "Dilip"
a.dob=772016




dilip = Students("Dilip",16,100,6,"Cricket")


darshan = Students("Darshan",17,99,7,"Running")


shruti = Students("Darshan",18,98,8,"Jumping")


harish = Students("Harish",19,97,9,"Hockey")


sam = Students("Sam",20,96,10,0)


pers1 = Students("P1",21,95,5,"Football")


pers2 = Students("P2",22,94,4,"Shooting")


pers3 = Students("P3",23,93,3,"Soccer")


pers4 = Students("P4",24,92,3,"Ice Hockey")


pers5 = Students("p5",25,91,2,"Baseball")






ar=[0,1,2,3,4,6]

p=[11,12,14,15]

ar.append(p[3])


    

x=random.randrange(0,11)

