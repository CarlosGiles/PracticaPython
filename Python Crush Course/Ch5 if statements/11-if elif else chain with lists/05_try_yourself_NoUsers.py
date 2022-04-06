"""
5-9. No Users: Add an if test to hello_admin.py to make sure the list of users is
not empty
•	 If the list is empty, print the message We need to fnd some users!
•	 Remove all of the usernames from your list, and make sure the correct
message is printed
"""
usernames=['CarlosGiles','YamileZeron','JorgeGiles','RocioVega','CidGiles','admin']

if usernames:#this is "if the list is empty"
    print("We need to find some users")
else:
    for username in usernames:
        if username=='admin':
            print("Hello "+username+", would you like to see a status report?")
        else:
            print("Hello "+username+", thank you for logging in again!")