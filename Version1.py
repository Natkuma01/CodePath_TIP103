# class Node:
#    def __init__(self, value, next=None):
#        self.value = value
#        self.next = next

# # For testing
# def print_linked_list(head):
#     current = head
#     while current:
#         print(current.value, end=" -> " if current.next else "\n")
#         current = current.next

# def edit_dna_sequence(dna_strand, m, n):
#     curr = dna_strand
#     while curr:
#         for _ in range (1, m):
#             if not curr:
#                 return dna_strand
#             curr = curr.next
#         dummy = curr.next
#         for _ in range (n):
#             if not dummy:
#                 break
#             dummy = dummy.next
#         curr.next = dummy
#         curr = dummy
#     return dna_strand
            
# dna_strand = Node(1, Node(2, Node(3, Node(4, Node(5, Node(6, Node(7, Node(8, Node(9, Node(10, Node(11, Node(12, Node(13)))))))))))))

# print_linked_list(edit_dna_sequence(dna_strand, 2, 3))

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def cycle_length(protein):
    freq = {}
    curr = protein
    cycle = []
    while curr:
        if curr in freq:
            if freq[curr] == 2:
                break
            freq[curr] += 1
            cycle.append(curr.value)
        else:
            freq[curr] = 1 # here is bug (I had to put inside else) <-- yes now can print the answer
        curr = curr.next
    return cycle

# Thanks guys! its great discussion! Nice to work with u guys - Nat

protein_head = Node('Ala', Node('Gly', Node('Leu', Node('Val'))))
protein_head.next.next.next.next = protein_head.next 

print(cycle_length(protein_head))

