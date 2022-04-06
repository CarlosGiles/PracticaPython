"""
A few Python functions are specifc to lists of numbers. For example, you
can easily fnd the minimum, maximum, and sum of a list of numbers:
"""
digist=[]
for value in range(2,101,2):
    digist.append(value**2)
print("The list is: ",digist,"\n")
print("The min into the list is:")
print("\t")
print(min(digist))
print("The min into the list is:")
print("\t")
print(max(digist))
print("The sum of the numbers into the list is:")
print("\t")
print(sum(digist))

