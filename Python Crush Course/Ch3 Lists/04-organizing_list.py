"""
Python’s sort() method makes it relatively easy to sort a list. Imagine we
have a list of cars and want to change the order of the list to store them
alphabetically. To keep the task simple, let’s assume that all the values in
the list are lowercase
"""
cars=['tsuru','aveo','gol']
print(cars)
cars.sort()
print(cars)
"""
The sort() method, shown at line code, changes the order of the list permanently. 
The cars are now in alphabetical order, and we can never revert to the original order
"""
#You can also sort this list in reverse alphabetical order by passing the argument reverse=True to the sort() method
cars.sort(reverse=True)
print(cars)
"""
To maintain the original order of a list but present it in a sorted order, you
can use the sorted() function. The sorted() function lets you display your list
in a particular order but doesn’t affect the actual order of the list
"""
#Sorting a List Temporarily with the sorted() Function
cars2=['tsuru','aveo','gol','audi','civic']
print("Here is the second original list: ",cars2)
print("Here is the sorted second list: ",sorted(cars2))#alphabetical order
print("Here is the second original list again: ",cars2)#list is not modified
#Reverse method
cars2.reverse()
print(cars2)#Notice that reverse() doesn’t sort backward alphabetically; it simply reverses the order of the list:
cars2.reverse()#the original list again
print(cars2)
"""
The reverse() method changes the order of a list permanently, but you
can revert to the original order anytime by applying reverse() to the same
list a second time
"""
#Finfing the lenght of a list
print("Lenght of the lis: ",len(cars2))

