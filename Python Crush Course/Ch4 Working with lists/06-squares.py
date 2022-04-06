"""
You can create almost any set of numbers you want to using the range()
function. For example, consider how you might make a list of the frst 10
square numbers (that is, the square of each integer from 1 through 10). In
Python, two asterisks (**) represent exponents. Here’s how you might put
the frst 10 square numbers into a list:
"""
#squares=[]
#for value in range(1,11):
#    square=value**2
#    squares.append(square)
#print(squares)
"""
To write this code more concisely, omit the temporary variable square
and append each new value directly to the list:
"""
squares=[]
for value in range(1,11):
    squares.append(value**2)
print(squares)