# ================ Problem 1 ====================
# change arr into linked list
class Player:
    def __init__(self, character, kart):
        self.character = character
        self.kart = kart
        self.items = []

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

# For testing
def print_linked_list(head):
    current = head
    while current:
        print(current.value.character, end=" -> " if current.next else "\n")
        current = current.next

def arr_to_ll(arr):
    if not arr:
        return None
    
    dummy = Node(0)             # create dummy node
    curr = dummy
    for value in arr:                   # loop through the array
        curr.next = Node(value)         # set curr.next as a code
        curr = curr.next                # shift curr to next 
    return dummy.next

print("================ Problem 1 ====================")
mario = Player("Mario", "Mushmellow")
luigi = Player("Luigi", "Standard LG")
peach = Player("Peach", "Bumble V")

print_linked_list(arr_to_ll([mario, luigi, peach]))
print_linked_list(arr_to_ll([peach]))



# ================ Problem 2 ====================
class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

# For testing
def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> " if current.next else "\n")
        current = current.next

# Function with a bug!
def remove_by_value(head, val):
    if not head:
        return None
    if head.value == val:
        return head.next  

    current = head
    while current.next:
        if current.next.value == val:
            current.next = current.next.next  
            return head  
        current = current.next

    return head


print("================ Problem 2 ====================")
head = Node("Daisy", Node("Mario", Node("Waluigi", Node("Baby Peach"))))

print_linked_list(remove_by_value(head, "Waluigi"))



# ================ Problem 3 ====================
# Understand: create two linked list, one is less, one is greater
#             connect them both togather
# Plan: create two dummy node, create two tails 
#       allocate the value to both linked list properly
#       set the end of the greater list end of pointing to None
#       link the two list together
#       return the less list.next

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

def partition(head, val):
    dummy_less = Node(0)                # head
    dummy_greater = Node(0)
    less = dummy_less                   # tail
    greater = dummy_greater

    curr = head
    while curr:
        if curr.value >= val:
            greater.next = curr
            greater = greater.next
        else:
            less.next = curr
            less = less.next
        curr = curr.next

    greater.next = None         # prevent cycle
    less.next = dummy_greater.next

    return dummy_less.next

print("================ Problem 3 ====================")
head = Node(1, Node(4, Node(3, Node(2, Node(5, Node(2))))))

print_linked_list(partition(head, 3))


# ================ Problem 4 ====================
# when fast pointer go 2 steps fastere, slow pointers in the middle of the list
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

def middle_match(head, val):
    slow = head
    fast = head
   

    while fast and fast.next: 
        slow = slow.next
        fast = fast.next.next
    if  slow.value == val:
        return True
    else:
        return False
    

print("================ Problem 4 ====================")
kart_choices = Node("Bullet Bike", Node("Wild Wing", Node("Pirahna Prowler")))
tournament_tracks = Node("Rainbow Road", Node("Bowser Castle", Node("Sherbet Land", Node("Yoshi Valley"))))

print(middle_match(kart_choices, "Wild Wing"))
print(middle_match(tournament_tracks, "Bowser Castle"))



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


def reverse(head):
    prev = None
    curr = head
    
    while curr: 
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node

    return prev

print("================ Problem 5 ====================")
kart_choices = Node("Bullet Bike", Node("Wild Wing", Node("Pirahna Prowler")))

print_linked_list(reverse(kart_choices))



# ================ Problem 6 ====================
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

def is_symmetric(head):
    arr = []
    curr = head
    while curr:
        arr.append(curr.value)
        curr = curr.next
    return arr == arr[::-1]

print("================ Problem 6 ====================")
head1 = Node("Bitterling", Node("Crawfish", Node("Bitterling")))
head2 = Node("Bitterling", Node("Carp", Node("Koi")))

print(is_symmetric(head1))
print(is_symmetric(head2))