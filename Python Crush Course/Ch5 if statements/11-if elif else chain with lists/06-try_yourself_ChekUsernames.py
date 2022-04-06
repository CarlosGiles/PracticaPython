"""
5-10. Checking Usernames: Do the following to create a program that simulates
how websites ensure that everyone has a unique username
•	 Make a list of five or more usernames called current_users
•	 Make another list of five usernames called new_users. Make sure one or
two of the new usernames are also in the current_users list
•	 Loop through the new_users list to see if each new username has already
been used. If it has, print a message that the person will need to enter a
new username. If a username has not been used, print a message saying
that the username is available
•	 Make sure your comparison is case insensitive. If 'John' has been used,
'JOHN' should not be accepted 'carlosGiles','carlosgiles','CARLOSGILES'
"""
current_users=['CarlosGiles','YamileZeron','JorgeGiles','RocioVega','CidGiles']
new_users=['CidGiles','YairZeron','MarlonZeron','GinnaBolivar','YamileZeron','CARLOSGILES','carlosGiles','carlosgiles']
#lista con los mismos usuarios que current_liist pero en minus para usarlos en validación:
current_users_validation=[user.lower() for user in current_users]
#si se introduce un usuario con mayus, el prog lo convierte en minus dentro de la lista
#y si se encuentra en current_users_validation lo pasará como inválido
for new_user in new_users:#por cada nuevo usuario...
    if new_user.lower() in current_users_validation:#... se usará su versión en minus para validar
        print("Sorry, the username '"+new_user+"' is not available, you will need to enter a new username")
    else:
        print("Good! The username '"+new_user+"' is available")

