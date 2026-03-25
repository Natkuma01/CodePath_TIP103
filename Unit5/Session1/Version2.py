# ================ Problem 1 ====================
class Player:
    def __init__(self, character, kart):
        self.character = character
        self.kart = kart
        self.items = []

print("================ Problem 1 ====================")
player_one = Player("Yoshi", "Super Blooper")
print(player_one.character)
print(player_one.kart) 
print(player_one.items)



# ================ Problem 2 ====================
class Player:
    def __init__(self, character, kart):
        self.character = character
        self.kart = kart
        self.items = []
        
    def add_item(self, item_name):
        self.items.append(item_name)
    

print("================ Problem 2 ====================")
player_one = Player("Yoshi", "Dolphin Dasher")
print(player_one.items)

player_one.add_item("red shell")
print(player_one.items)

player_one.add_item("super star")
print(player_one.items)

player_one.add_item("super smash")
print(player_one.items)



# ================ Problem 3 ====================
class Player:
    def __init__(self, character, kart):
        self.character = character
        self.kart = kart
        self.items = []
    # ... methods from previous problems

def print_results(race_results):
    pass


print("================ Problem 3 ====================")
peach = Player("Peach", "Daytripper")
mario = Player("Mario", "Standard Kart M")
luigi = Player("Luigi", "Super Blooper")
race_one = [peach, mario, luigi]

print_results(race_one)