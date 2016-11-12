def hotel_cost(nights):
    return 140*nights

def plane_ride_cost (city):
    if city == "Charlotte":
        fcost = 183
        return fcost
    
    if city == "Tampa":
        fcost = 220
        return fcost
    
    if city == "Pittsburgh":
        fcost = 222
        return fcost
    
    if city == "Los Angeles":
        fcost = 475
        return fcost

def rental_car_cost(days):
    ccost = days*40
    if ccost>=280:
        ccost-=50
    elif ccost>=120 and ccost<280:
        ccost-=20
    return ccost    
    
def trip_cost (city, days, spending_money):
   return plane_ride_cost(city)+rental_car_cost(days)+hotel_cost(days)+spending_money

'''print "THE TRIP COST FINDER"
city = raw_input("Enter the city you wish to travel to")
days = raw_input("Enter the number of days")
spending_money = raw_input("Enter the amount of money you'd like to spend on this trip")
trip_cost(city, days, spending_money)'''