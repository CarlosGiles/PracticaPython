"""
Python cannot concatenate numbers without converting them to strings
"""

age=28
#message1="Happy"+age+"rd Birthday"
message2="Happy "+str(age)+"rd Birthday"
#message1 should give an error
print(message2)
#print(message1)