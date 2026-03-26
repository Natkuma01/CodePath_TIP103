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
    def add_item(self, item_name):
        self.items.append(item_name)

def print_results(race_results):
    for item in race_results:
        print(item.character)


print("================ Problem 3 ====================")
peach = Player("Peach", "Daytripper")
mario = Player("Mario", "Standard Kart M")
luigi = Player("Luigi", "Super Blooper")
race_one = [peach, mario, luigi]

print_results(race_one)


# ================ Problem 4 ====================
class Player:
    def __init__(self, character, kart, opponent=None):
        self.character = character
        self.kart = kart
        self.items = []
        self.ahead = opponent

def get_place(my_player):
    place = 1
    curr = my_player
    while curr.ahead:
        place += 1
        curr = curr.ahead
    return place
    

print("================ Problem 4 ====================")
peach = Player("Peach", "Daytripper")
mario = Player("Mario", "Standard Kart M", peach)
luigi = Player("Luigi", "Super Blooper", mario)

player1_rank = get_place(luigi)
player2_rank = get_place(peach)
player3_rank = get_place(mario)

print(player1_rank)
print(player2_rank)
print(player3_rank)


# ================ Problem 5 ====================
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

# For testing
def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> " if current.next else "\n")
        current = current.next

daisy = Node("Daisy")
peach = Node("Peach")
luigi = Node("Luigi")
mario = Node("Mario")

daisy.next = peach
peach.next = luigi
luigi.next = mario

print("================ Problem 5 ====================")
print_linked_list(daisy)


# ================ Problem 6 ====================
class Node:
    def __init__(self, player, next=None):
        self.player_name = player
        self.next = next

# For testing
def print_linked_list(head):
    current = head
    while current:
        print(current.player_name, end=" -> " if current.next else "\n")
        current = current.next

def count_racers(head):
    count = 0
    curr = head
    while curr:
        count += 1
        curr = curr.next
    return count

print("================ Problem 6 ====================")
racers1 = Node("Mario", Node("Peach", Node("Luigi", Node("Daisy"))))
racers2 = Node("Mario")

print(count_racers(racers1))
print(count_racers(racers2))
print(count_racers(None))


# ================ Problem 7 ====================
class Node:
    def __init__(self, player, next=None):
        self.player_name = player
        self.next = next

# For testing
def print_linked_list(head):
    current = head
    while current:
        print(current.player_name, end=" -> " if current.next else "\n")
        current = current.next

def last_place(head):
    if not head:
        return None
    
    curr = head
    while curr.next:
        curr = curr.next
    return curr.player_name

print("================ Problem 7 ====================")
racers1 = Node("Mario", Node("Peach", Node("Luigi", Node("Daisy"))))
racers2 = Node("Mario")

print(last_place(racers1)) 
print(last_place(racers2)) 
print(last_place(None))


# ================ Problem 8 ====================
class Node:
    def __init__(self, player, next=None):
        self.player_name = player
        self.next = next

# For testing
def print_linked_list(head):
    current = head
    while current:
        print(current.player_name, end=" -> " if current.next else "\n")
        current = current.next

def increment_rank(head, target):
    if target <= 1 or not head:
        return head
    
    curr = head
    prev = None
    count = 1
    while count < target:
        prev = curr
        curr = curr.next
        count += 1

    temp = prev.player_name
    prev.player_name = curr.player_name
    curr.player_name = temp

    return head



print("================ Problem 8 ====================")
racers1 = Node("Mario", Node("Peach", Node("Luigi", Node("Daisy"))))
racers2 = Node("Mario", Node("Luigi"))

print_linked_list(increment_rank(racers1, 3))
print_linked_list(increment_rank(racers2, 1)) 
print_linked_list(increment_rank(None, 1)) 