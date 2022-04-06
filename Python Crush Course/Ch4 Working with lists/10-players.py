"""
slice: print indexs from 0 to 2 (3 indexs)
"""
players=['carlos','yamile','jorge','cid','rocio']
print(players[0:3])
"""
If you omit the frst index in a slice, Python automatically starts your
slice at the beginning of the list:
"""
print(players[:4])
"""
if you want all items from the third item through the last item,
you can start with index 2 and omit the second index:
"""
print(players[2:])
"""
if we want to output the last three players on the roster, we can use the slice
players[-3:]:
"""
print(players[-3:])

print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())
