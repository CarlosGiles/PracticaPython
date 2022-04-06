"""
Let’s reconsider the pizzeria example. If someone requests a two-topping
pizza, you’ll need to be sure to include both toppings on their pizza:
"""
resquested_toppings=['mushrooms','extra cheese']

if 'mushrooms' in resquested_toppings:
    print("Adding mushrooms.")
elif ' pepperoni' in resquested_toppings:
    print("Adding pepperoni.")
elif 'extra cheese' in resquested_toppings:
    print("Adding extra cheese.")

print("\n Finished making your pizza!")

"""
The test for 'mushrooms' is the frst test to pass, so mushrooms are added
to the pizza. However, the values 'extra cheese' and 'pepperoni' are never
checked, because Python doesn’t run any tests beyond the frst test that
passes in an if-elif-else chain. The customer’s frst topping will be added,
but all of their other toppings will be missed
"""
#----------------------------------------------------------------------------
if 'mushrooms' in resquested_toppings:
    print("Adding mushrooms.")
if ' pepperoni' in resquested_toppings:
    print("Adding pepperoni.")
if 'extra cheese' in resquested_toppings:
    print("Adding extra cheese.")

print("\n Finished making your pizza!")