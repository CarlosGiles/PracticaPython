"""
In this example, range() prints only the numbers 1 through 4. This is
another result of the off-by-one behavior you’ll see often in programming
languages. The range() function causes Python to start counting at the frst
value you give it, and it stops when it reaches the second value you provide
"""
for value in range(1,5):
    print(value)
print("----------------------------------------")
"""
Because it stops at that second value, the output never contains the end
value, which would have been 5 in this case.
To print the numbers from 1 to 5, you would use range(1,6):
"""
for value in range(1,6):
    print(value)