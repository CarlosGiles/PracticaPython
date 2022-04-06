"""
4-3. Counting to Twenty: Use a for loop to print the numbers from 1 to 20,
inclusive
"""
numbers=[]
for number in range(1,21):
    numbers.append(number)
print("The list of numbers is: ",numbers)

"""
4-4. One Million: Make a list of the numbers from one to one million, and then
use a for loop to print the numbers (If the output is taking too long, stop it by
pressing ctrl-C or by closing the output window )
"""
millionList=[]
for numberM in range(1,1000001):
    millionList.append(numberM)
    #print(numberM) because the output is taking too long
"""
use min() and max() to make sure your list actually starts at one and
ends at one million Also, use the sum() function to see how quickly Python can
add a million numbers
"""
print("The min in the list:")
print(min(millionList))
print("The max in the list:")
print(max(millionList))
print("The sum of de numbers into de list:")
print(sum(millionList))
"""
Odd Numbers: Use the third argument of the range() function to make a list
of the odd numbers from 1 to 20 Use a for loop to print each number
"""
oddnumbers=[]
for oddnumber in range(1,20,2):
    oddnumbers.append(oddnumber)
    print("Number in list: ",oddnumber)
print("The odd numbers list: ",oddnumbers)
"""
Threes: Make a list of the multiples of 3 from 3 to 30 Use a for loop to
print the numbers in your list
"""
threes=[]
for value in range(3,31,3):
    threes.append(value)
print("Values from three's table: ",threes)
"""
Cube Comprehension: Use a list comprehension to generate a list of the
frst 10 cubes
"""
cubelist=[value**3 for value in range(1,11)]
print("The first 10 cubes are: ",cubelist)