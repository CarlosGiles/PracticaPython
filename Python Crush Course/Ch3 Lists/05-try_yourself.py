"""
Think of at least five places in the world you’d like to
visit
"""
places=['paris','stonehenge','rapanui','korea','suiza']
print("The original list: ",places)
#Use sorted() to print your list in alphabetical order without modifying the actual list
print("The sorted list in alphabetical order is: ",sorted(places))
print("List is still in its original order: ",places)
#Use sorted() to print your list in reverse alphabetical order without changing the order of the original list

#places.sort(reverse=True)
#print(places)

places2=sorted(places)
places2.reverse()
print("The list in reverse alphabetical order whithout changing the original list is: ",places2)

#Show that your list is still in its original order by printing it again
print("The list still is: ",places)
places.reverse()
print("The original list in reverse mode is: ",places)
#Reverse again for became to original list
places.reverse()
print("Again, the original list is: ",places)
#Use sort() to change your list so it’s stored in alphabetical order Print the list to show that its order has been changed
places.sort()
print("The list has changed to alphabetical order: ",places)
places.sort(reverse=True)
print("The list has changed to reverse alphabetical order: ",places)
