players = ("Messi","Ronaldo","Neymar","Mbappe","Haaland")

# Unpack first two players, and store the rest in a list
(first1,first2,*restPlayers) = players
print(first1)
print(first2)
print(restPlayers)

# Unpack all except the last player, store last player separately
(*startPlayers,lastPlayer) = players
print(startPlayers)
print(lastPlayer)

# Unpack first and last players, and store the middle ones in a list
(firstPlayer,*middlePlayers,lastPlayer2) = players
print(firstPlayer)
print(middlePlayers)
print(lastPlayer2)
