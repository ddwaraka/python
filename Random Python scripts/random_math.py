import math

def polygon_area(no_of_sides, side_length):
    print (0.25*no_of_sides*side_length**2) / math.tan(math.pi/no_of_sides)

polygon_area(5,7)
polygon_area(7,3)