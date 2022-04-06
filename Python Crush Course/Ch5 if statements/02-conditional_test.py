"""
Testing for equality is case sensitive in Python. For example, two values with
different capitalization are not considered equal
"""
car='bmw'
if car=='bmw':
    print("True")
else:
    print("False")

car='Bmw'
if car=='bmw':
    print("True")
else:
    print("False")

car = 'Audi'
if car.lower()=='audi':
    print("True")
else:
    print("False")

requested_topping = 'mushrooms'
if requested_topping != 'anchovies':
    print("Hold the anchovies!")


