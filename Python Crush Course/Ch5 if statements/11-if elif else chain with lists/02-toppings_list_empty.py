"""
As an example, let’s check whether the list of requested toppings is
empty before building the pizza. If the list is empty, we’ll prompt the user
and make sure they want a plain pizza. If the list is not empty, we’ll build
the pizza just as we did in the previous examples:
"""
resquested_toppings=[]
if resquested_toppings:
    for resquested_topping in resquested_toppings:
        print("Adding "+resquested_topping+".")
else:
        print("Are you sure you want a plain pizza?")
#If the list is not empty, the output will show each requested topping being added to the pizza