"""
if we have a rectangle that should always be a certain size,
we can ensure that its size doesn’t change by putting the dimensions into a
tuple
"""
dimensions=(200,50)
print(dimensions[0])
print(dimensions[1])
#Let’s see what happens if we try to change one of the items in the tuple dimensions
#dimensions[0]=250
"""
You can loop over all the values in a tuple using a for loop, just as you did
with a list
"""
dimensions = (200, 50)
for dimension in dimensions:
    print(dimension)