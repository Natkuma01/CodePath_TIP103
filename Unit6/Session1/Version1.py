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

def edit_dna_sequence(dna_strand, m, n):
    curr = dna_strand
    while curr:
        for _ in range (m-1):
            if not curr.next:
                return dna_strand
            curr = curr.next
        dummy = curr
        for _ in range (n):
            if not curr.next:
                break
            curr = curr.next
        dummy.next = curr.next
        curr = dummy.next
    return dna_strand
    

print("================ Problem 1 ====================")
dna_strand = Node(1, Node(2, Node(3, Node(4, Node(5, Node(6, Node(7, Node(8, Node(9, Node(10, Node(11, Node(12, Node(13)))))))))))))

print_linked_list(edit_dna_sequence(dna_strand, 2, 3))


# ================ Problem 2 ====================
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def cycle_length(protein):
    slow = protein
    fast = protein
    
    res = []
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            res.append(slow.value)
            slow = slow.next
            while slow != fast:
                res.append(slow.value)
                slow = slow.next
            return res


print("================ Problem 2 ====================")
protein_head = Node('Ala', Node('Gly', Node('Leu', Node('Val'))))
protein_head.next.next.next.next = protein_head.next 

print(cycle_length(protein_head))


# ================ Problem 3 ====================
# first find out what is the len linked list % k is 
# 
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

# For testing
def print_linked_list(head):
    if not head:
        print("Empty List")
        return
    current = head
    while current:
        print(current.value, end=" -> " if current.next else "\n")
        current = current.next

def split_protein_chain(protein, k):
    # find the length of linked list
    curr = protein
    total_nodes = 0
    while curr:
        curr = curr.next
        total_nodes += 1
    
    # find how many node should be in one group
    remainder = total_nodes % k
    quotient = total_nodes // k

    res = []
    curr = protein

    # take care of the extra node 
    while remainder > 0:
        head = curr
        for _ in range (quotient):
            curr = curr.next
        next_node = curr.next
        curr.next = None
        curr = next_node
        remainder -= 1
        res.append(head)

    while curr:
        head = curr
        for _ in range (quotient-1):
            curr = curr.next
        next_node = curr.next
        curr.next = None
        curr = next_node
        res.append(head)
    return res


print("================ Problem 3 ====================")
protein1 = Node('Ala', Node('Gly', Node('Leu', Node('Val', Node('Pro', Node('Ser', Node('Thr', Node('Cys'))))))))
protein2 = Node('Ala', Node('Gly', Node('Leu', Node('Val'))))

parts = split_protein_chain(protein1, 3)
for part in parts:
    print_linked_list(part)

parts = split_protein_chain(protein2, 5)
for part in parts:
    print_linked_list(part)



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

def max_protein_pair_stability(head):
    arr = []
    curr = head
    while curr:
        arr.append(curr.value)
        curr = curr.next

    n = len(arr)
    largest = 0

    for i in range (n):
        twin_sum = arr[i] + arr[n-1-i]
        largest = max(largest, twin_sum)
    return largest


print("================ Problem 4 ====================")
head1 = Node(5, Node(4, Node(2, Node(1))))
head2 = Node(4, Node(2, Node(2, Node(3))))

print(max_protein_pair_stability(head1))
print(max_protein_pair_stability(head2))


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

def odd_even_experiments(exp_results):
    odd = Node(0)                   # head
    even = Node(0)
    odd_tail = odd                  # tail
    even_tail = even

    curr = exp_results
    while curr:
        odd_tail.next = curr
        odd_tail = odd_tail.next
        if not curr.next:                   # set odd tail point to None
            odd_tail.next = None
            break
        curr = curr.next
        even_tail.next = curr
        even_tail = even_tail.next
        curr = curr.next

    odd_tail.next = even.next               # link the odd tail to the even head
    even_tail.next = None                   # even tail point to None

    return odd.next
print("================ Problem 5 ====================")
experiment_results1 = Node(1, Node(2, Node(3, Node(4, Node(5)))))
experiment_results2 = Node(2, Node(1, Node(3, Node(5, Node(6, Node(4, Node(7)))))))

print_linked_list(odd_even_experiments(experiment_results1))
print_linked_list(odd_even_experiments(experiment_results2))