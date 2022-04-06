resquested_toppings=['mushrooms','green peppers','extra cheese']
for resquested_topping in resquested_toppings:
    print("Adding "+resquested_topping+"....")
print("\nFinished making your pizza!")

"""
But what if the pizzeria runs out of green peppers? An if statement inside
the for loop can handle this situation appropiately
"""
resquested_toppings=['mushrooms','green peppers','extra cheese']
for resquested_topping in resquested_toppings:
    if resquested_topping=='green peppers':
        print("Sorry, we are out of green peppers right now.")
    else:
        print("Adding "+resquested_topping+".")
print("\nFinished making your pizza!")