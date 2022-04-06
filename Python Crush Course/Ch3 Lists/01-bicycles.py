"""
square brackets ([]) indicate a list, and individual elements
in the list are separated by commas. Here’s a simple example of a list that
contains a few kinds of bicycles
"""
bicycles=['trek','redline','cannondale','specialized']
"""If you ask Python to print a list, Python returns its representation of the
list, including the square brackets
"""
print(bicycles)

"""
To access an element in a list, write the name of the list followed by the index of the item
enclosed in square brackets. The index starts in 0
"""
print("The first element in the list is: ",bicycles[0])
print("The first element in the list is: ",bicycles[0].title())#This example produces the same output as the preceding example except 'Trek' is capitalized

"""
Python has a special syntax for accessing the last element in a list. By asking for the item at index -1, 
Python always returns the last item in the list:
"""

print("The last item in list has an index -1: ",bicycles[-1])
#Armamos un mensaje convatenando datos y metodos
message = "My first bicycle was a " + bicycles[0].title() + "."
print(message)