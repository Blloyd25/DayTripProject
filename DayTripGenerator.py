
import random

destination = ['Napa Valley', 'Dallas', 'New York', 'Orlando', 'Boston']
location = random.choice(destination)
print(location)

def promt_destination (location):
    user_choice = input("do you wish to keep this destination?" +  ' ' +  "type yes or no" + ' ')
    
    if user_choice == 'no':
     location = random.choice(destination)   
     print(location)
     return promt_destination(location)
     
    if user_choice == 'yes':
        print(location + ' is your selected destination')
        return location
     
final_destination=promt_destination(location)

restaurants = ['Pizza', 'Sushi', 'Pasta', 'Sandwiches', 'ethnic']
places_to_eat = random.choice(restaurants)
print(places_to_eat)

def promt_restaurant (places_to_eat):
    user_choice = input("do you wish to keep this restaurant?" +  ' ' +  "type yes or no" + ' ')
    if user_choice == 'no':
     places_to_eat = random.choice(restaurants)   
     print(places_to_eat)
     return promt_restaurant(places_to_eat)
     
    if user_choice == 'yes':
        print(places_to_eat + ' is your selected food type')
        return places_to_eat

final_restaurant=promt_restaurant(places_to_eat)

mode_of_transportation = ['flying', 'train', 'car', 'bus', 'uber']
ride = random.choice(mode_of_transportation)
print(ride)

def promt_mode_of_transportation(ride):
    user_choice = input("do you wish to keep this form of travel" + ' ' + "type yes or no")
    if user_choice == 'no':
     ride = random.choice(mode_of_transportation)
     print(ride)
     return promt_mode_of_transportation(ride)

    if user_choice == 'yes':
        print(ride + ' is your selected travel mode')
        return ride

final_transportation=promt_mode_of_transportation(ride)

entertainment = ['bar', 'nightclub', 'circus', 'festival', 'sports game']
what_to_do = random.choice(entertainment)
print(what_to_do)

def promt_entertainment (what_to_do):
    user_choice = input("do you wish to keep this event?" +  ' ' +  "type yes or no" + ' ')
    if user_choice == 'no':
        what_to_do = random.choice(entertainment)
        print(what_to_do)
        return promt_entertainment(what_to_do)
    
    if user_choice == 'yes':
        print(what_to_do + ' is your selected activity for the day')
        return what_to_do
final_entertainment= promt_entertainment(what_to_do)

print(f'your trip is now completed')
 
print(f'Here is your complete itenary for your trip to {final_destination}, you will be eating {final_restaurant}, we are going to get there by {final_transportation}, and you will enjoy the {final_entertainment} at night!') 





















































