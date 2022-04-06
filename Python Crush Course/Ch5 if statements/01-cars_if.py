"""
The following code loops through a list of car
names and looks for the value 'bmw'. Whenever the value is 'bmw', it’s printed
in uppercase instead of title case
"""
cars=['audi','bmw','subaru','toyota']
for car in cars:
    if car=='bmw':
        print(car.upper())
    else:
        print(car.title())