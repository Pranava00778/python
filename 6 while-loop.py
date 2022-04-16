players =[]

doYouWantMore='y'
while doYouWantMore=='y':
    newPlayer = input("Add New Players Name: ")
    players.append(newPlayer)
    doYouWantMore = input("More: ")

print(players)
    