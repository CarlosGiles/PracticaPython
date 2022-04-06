"""
we’d have to change our code each time the list’s length changed. A for loop avoids both
of these issues by letting Python manage these issues internally.
Let’s use a for loop to print out each name in a list of magicians:
"""

magicians=['alice','david','carolina']

for magician in magicians:
    print(magician)

"""
We begin by defning a list at 1, just as we did in Chapter 3. At 2,
we defne a for loop. This line tells Python to pull a name from the list
magicians, and store it in the variable magician. At w we tell Python to print
the name that was just stored in magician. Python then repeats lines 2
and w, once for each name in the list. It might help to read this code as
“For every magician in the list of magicians, print the magician’s name.”
The output is a simple printout of each name in the list:
"""

#A new form to composse message
for magician in magicians:
    print(magician.title()+", that was a great trick!")
#Adding more code
for magician in magicians:
    print(magician.title()+", that was a great trick!")
    print("I can't wait to see your next trick. "+magician.title()+".\n")
print("Thank you, everyone. That was a great magic show!")