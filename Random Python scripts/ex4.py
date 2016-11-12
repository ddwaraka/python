cars=100
space=4.0
drivers=30
passengers=90
cars_not_driven=cars-drivers
cars_driven=drivers
carpool_capacity=cars_driven*space
average=passengers/cars_driven

print "cars = ",cars
print "space = ",space
print "drivers = ",drivers
print "passengers = ",passengers
print "cars not driven = ",cars_not_driven
print "cars driven = ",cars_driven
print "carpool capacity = ",carpool_capacity
print "average = ",average