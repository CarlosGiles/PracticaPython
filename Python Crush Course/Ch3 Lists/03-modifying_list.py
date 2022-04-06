"""
To change an element, use the name of the list followed
by the index of the element you want to change, and then provide the new
value you want that item to have.
"""
my_team=['Obi One','BD1','Ahsoka']
print("My team is: "+str(my_team))#only we concatenning str
#Modifying team:
my_team[1]='Qui-Gon Jinn'
print("But, I remove BD1 and add Qui-Gon: "+str(my_team))
#Adding new element
my_team.append('Anakin')
print("Now, I can add a new Knight and my new team is: "+str(my_team))
#Insertting new element in any index
my_team.insert(0,'Master Yoda')#add new element in pos 0
print("I have a new power, I summon Master Yoda as leader: "+str(my_team))
#Remove elements of he list
del my_team[3]
print("Unfortunately Ahsoka died"+str(my_team))
"""
removing an Item Using the pop() Method
The pop() method removes the last item in a list, but it lets you work
with that item after removing it. The term pop comes from thinking of a
list as a stack of items and popping one item off the top of the stack
"""
popped_my_team=my_team.pop()
print("After the battle, Jedi Knight Anakin goes: "+str(my_team))
print("Lost knight: "+str(popped_my_team))
"""
We started by defning and printing the list motorcycles at u. At v we pop
a value from the list and store that value in the variable popped_motorcycle.
We print the list at w to show that a value has been removed from the list.
Then we print the popped value at x to prove that we still have access to
the value that was removed.
"""
#Popping Items from any Position in a List
popped1_my_team=my_team.pop(1)
print("The Knight Jedi "+str(popped1_my_team+" set out in search of "+str(popped_my_team)))
"""
when you want to delete an item from a list
and not use that item in any way, use the del statement; if you want to use an
item as you remove it, use the pop() method.
"""
"""Sometimes you won’t know the position of the value you want to remove
from a list. If you only know the value of the item you want to remove, you
can use the remove() method.
"""
my_team.remove('Master Yoda')
print("Master Yoda ran out and left "+str(my_team))

#motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
#print(motorcycles)
#too_expensive = 'ducati'
#motorcycles.remove(too_expensive)
#print(motorcycles)
#print("\nA " + too_expensive.title() + " is too expensive for me.")