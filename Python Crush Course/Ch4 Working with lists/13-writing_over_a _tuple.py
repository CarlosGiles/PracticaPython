"""
Although you can’t modify a tuple, you can assign a new value to a variable
that holds a tuple. So if we wanted to change our dimensions, we could
redefne the entire tuple
"""
dimensions = (200, 50)
print("Original dimensions:")
for dimension in dimensions:
    print(dimension)
dimensions = (400, 100)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)
"""
The block at u defnes the original tuple and prints the initial dimensions. At v, we store a new tuple in the variable dimensions. We then print the
new dimensions at w. Python doesn’t raise any errors this time, because
overwriting a variable is valid
"""