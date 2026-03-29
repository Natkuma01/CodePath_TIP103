# ================ Problem 1 ====================
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

def find_max(head):
    curr = head
    largest = 0
    while curr:
        if curr.value > largest:
            largest = curr.value
        curr = curr.next
    return largest

print("================ Problem 1 ====================")
head1 = Node(5, Node(6, Node(7, Node(8))))

# Linked List: 5 -> 6 -> 7 -> 8
print(find_max(head1))

head2 = Node(5, Node(8, Node(6, Node(7))))

# Linked List: 5 -> 8 -> 6 -> 7
print(find_max(head2))



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

def remove_tail(head):
    if head is None:
        return None
    if head.next is None:
        return None 
        
    current = head
    while current.next.next: 
        current = current.next

    current.next = None 
    return head

print("================ Problem 2 ====================")
head = Node("Isabelle", Node("Alfonso", Node("Cyd")))

# Linked List: Isabelle -> Alfonso -> Cyd
print_linked_list(remove_tail(head))


# ================ Problem 3 ====================
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

def delete_dupes(head):
    dummy = Node(0, head)
    prev = dummy

    while prev.next:
        curr = prev.next
        if curr.next and curr.value == curr.next.value:
            while curr.next and curr.value == curr.next.value:
                curr = curr.next
            prev.next = curr.next
        else:
            prev = prev.next
    return dummy.next


print("================ Problem 3 ====================")
head = Node(1, Node(2, Node(3, Node(3, Node(4, Node(5))))))

# Linked List: 1 -> 2 -> 3 -> 3 -> 4 -> 5
print_linked_list(delete_dupes(head))
head1 = Node(2, Node(2, Node(3, Node(3, Node(3, Node(5))))))
print_linked_list(delete_dupes(head1))


# ================ Problem 4 ====================
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def has_cycle(head):
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False

print("================ Problem 4 ====================")
peach = Node("Peach", Node("Luigi", Node("Mario", Node("Toad"))))

# Toad.next = Luigi
peach.next.next.next = peach.next

print(has_cycle(peach))


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

def remove_nth_from_end(head, n):
    curr = head
    count = 1
    while curr:
        curr = curr.next
        count += 1

    n = count - n
    
    i = 0
    curr = head
    while i < n and curr.next:
        curr = curr.next
        i += 1
    curr.next = None

    return head
print("================ Problem 5 ====================")
head1 = Node("apple", Node("cherry", Node("orange", Node("peach", Node("pear")))))
head2 = Node("Rainbow Trout", Node("Ray"))
head3 = Node("Rainbow Stag")
print_linked_list(remove_nth_from_end(head1, 2))
# print_linked_list(remove_nth_from_end(head2, 1))
# print_linked_list(remove_nth_from_end(head3, 1))