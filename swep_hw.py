# In Candy Grab, players take turns to grab as much candy as they can. The game
# is played on a board with M x N cells. A candy is placed on top of every cell
# of the board. A character (i.e. =, +, %, etc.) represents a candy type.

# In a turn, a player chooses a candy from the board. Then, the player is allowed
# to grab that candy, and any other candy of the same type that is connected in
# any direction to it (up, down, left, right, diagonal).

# Let's use this board as example:

#    0 1 2 3 4 5 6 7 8 
# 0 |#|#|=|=|=|*|*|@|@|
# 1 |#|#|=|@|@|*|*|@|@|
# 2 |#|#|@|@|@|*|*|@|%|
# 3 |+|+|=|=|*|*|@|@|%|
# 4 |+|+|+|+|*|@|@|@|%|

# if a player chooses the candy placed in (row 0, column 2), then it will take
# *4* candies (of type `=`) in total: the selected candy, the one down from it,


# and the two candies to the right. 

# Write a function that takes as input the map, and a candy type, and returns the
# maximum amount of candies that a player can take in a single turn.

# For example, using as input the map above:

# find_largest_candy_group(map, '=') -> 4
# find_largest_candy_group(map, '@') -> 10
# find_largest_candy_group(map, '%') -> 3
