"""
We can also use the range() function to tell Python to skip numbers
in a given range. For example, here’s how we would list the even numbers
between 1 and 10:
"""
#In this example, the range() function starts with the value 2 and then adds 2 to that value. It adds 2 repeatedly until it reaches or passes the end value, 11
ever_numbers=list(range(2,11,2))
print(ever_numbers)