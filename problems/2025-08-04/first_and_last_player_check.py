# Problem: First & Last Player Check
# Description: Given a tuple or list of player names, check whether the first and last players are the same.
# If they are the same, print "Same", otherwise print "Different".

playerNumber = int(input("Enter number of player: "))

players = tuple(input("Enter player name:") for _ in range(playerNumber))

if players[0] == players[playerNumber - 1]:
    print("Same")
else:
    print("Different")