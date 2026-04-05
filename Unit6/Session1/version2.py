# ================ Problem 1 ====================
# the first node consider as even-indexed, second node is odd-indexed
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

def game_result(head):
    curr = head
    odd_count, odd_value = 0, 0
    even_count, even_value = 0, 0

    while curr:
        even_value = curr.value
        curr = curr.next
        odd_value = curr.value
        curr = curr.next
            
        if odd_value > even_value:
            odd_count += 1
        else:
            even_count += 1
        
    if odd_count > even_count:
        return "odd"
    elif odd_count == even_count:
        return "tie"
    else:
        return "even"

print("================ Problem 1 ====================")
game1 = Node(2, Node(1))
game2 = Node(2, Node(5, Node(4, Node(7, Node(20, Node(5))))))
game3 = Node(4, Node(5, Node(2, Node(1))))

print(game_result(game1))
print(game_result(game2))
print(game_result(game3))


# ================ Problem 2 ====================
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def cycle_start(path_start):
    slow = path_start
    fast = path_start

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return slow.next.value
    return None


print("================ Problem 2 ====================")
path_start = Node('Start', Node('Point 1', Node('Point 2', Node('Point 3'))))
path_start.next.next.next.next = path_start.next
print(cycle_start(path_start))



# ================ Problem 3 ====================
# Insertion sorted linked list
# the current node while traverse, is keep comparing with the first node (prev_node.next)
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

def sort_list(head):
    if not head:
        return None
    
    dummy = Node(0)
    curr = head

    while curr:
        next_node = curr.next
        prev_node = dummy

        while prev_node.next and prev_node.next.value < curr.value:
            prev_node = prev_node.next
        
        curr.next = prev_node.next
        prev_node.next = curr

        curr = next_node

    return dummy.next

print("================ Problem 3 ====================")
head1 = Node(4, Node(2, Node(1, Node(3))))
head2 = Node(-1, Node(5, Node(3, Node(4, Node(0)))))

print_linked_list(sort_list(head1))
print_linked_list(sort_list(head2))



# ================ Problem 4 ====================
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

def add_two_numbers(head_a, head_b):
    curr_a = head_a
    curr_b = head_b
    str_a = []
    str_b = []

    # combine each value into a str
    while curr_a:
        str_a.append(str(curr_a.value)) 
        curr_a = curr_a.next

    while curr_b:
        str_b.append(str(curr_b.value)) 
        curr_b = curr_b.next
    
    total = str(int("".join(str_a)) + int("".join(str_b)))[::-1]

    dummy = Node(0)
    curr = dummy

    for num in total:
        curr.next = Node(num)
        curr = curr.next
    return dummy.next
    

print("================ Problem 4 ====================")
head_a = Node(2, Node(4, Node(3))) # 342
head_b = Node(5, Node(6, Node(4))) # 465

print_linked_list(add_two_numbers(head_a, head_b))



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

def next_highest_scoring_contestant(contestant_scores):
    res = []
    stack = []

    curr = contestant_scores
    while curr:
        if not stack:
            stack.append(curr.value)
        elif curr.value < stack[-1]:
            stack.append(curr.value)
        else:
            for _ in range (len(stack)):
                res.append(curr.value)
            res.append(0)
            stack.clear()
        curr = curr.next
    return res

print("================ Problem 5 ====================")
contestant_scores1 = Node(2, Node(1, Node(5)))
contestant_scores2 = Node(2, Node(7, Node(4, Node(3, Node(5)))))

print(next_highest_scoring_contestant(contestant_scores1))
print(next_highest_scoring_contestant(contestant_scores2))