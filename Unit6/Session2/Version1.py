# ================ Problem 1 ====================
# Queue + Linked List
class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next = next

# For testing
def print_queue(head):
    current = head.front
    while current:
        print(current.value, end=" -> " if current.next else "")
        current = current.next
    print()

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
    
    def is_empty(self):
        return self.front == None

    def enqueue(self, song_artist_pair):
        new_node = Node(song_artist_pair)
        if self.is_empty():
             self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
    
    def dequeue(self):
        if self.is_empty():
            return None
        temp = self.front.value
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        return temp
    
    def peek(self):
        if self.is_empty():
            return None
        return self.front.value

print("================ Problem 1 ====================")
# Create a new Queue
q = Queue()

# Add elements to the queue
q.enqueue(('Love Song', 'Sara Bareilles'))
q.enqueue(('Ballad of Big Nothing', 'Elliot Smith'))
q.enqueue(('Hug from a Dinosaur', 'Torres'))
print_queue(q)

# # View the front element
print("Peek: ", q.peek()) 

# # Remove elements from the queue
print("Dequeue: ", q.dequeue()) 
print("Dequeue: ", q.dequeue()) 

# # Check if the queue is empty
print("Is Empty: ", q.is_empty()) 

# # Remove the last element
print("Dequeue: ", q.dequeue()) 

# Check if the queue is empty
print("Is Empty:", q.is_empty()) 



# ================ Problem 2 ====================
class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next = next

# For testing
def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> " if current.next else "")
        current = current.next
    print()

def merge_playlists(playlist1, playlist2, a, b):
    curr = playlist1
    for _ in range (a-1):
        curr = curr.next
    prev = curr                         # hold on for the last node at the first part of playlist1

    for _ in range (b-a + 2):           
        prev = prev.next
    last_part_playlist1 = prev          # save the last part of the playlist1

    curr.next = playlist2               # connect the first part of playlist1 with playlist 2

    while curr.next:                    # add the last part of playlist1 at the end of playlist2
        curr = curr.next
    curr.next = last_part_playlist1

    return playlist1

print("================ Problem 2 ====================")
playlist1 = Node(('Flea', 'St. Vincent'),
                Node(('Juice', 'Lizzo'), 
                    Node(('Tenderness', 'Jay Som'),
                        Node(('Ego Death', 'The Internet'),
                            Node(('Empty', 'Kevin Abstract'))))))

playlist2 = Node(('Dreams', 'Solange'), Node(('First', 'Gallant')))

print_linked_list(merge_playlists(playlist1, playlist2, 2, 3))



# ================ Problem 3 ====================
# merged two linked list with O(1) space - no array
# Reorder the linked list - 1 -> 2 -> 3 -> 4 TO 1 -> 4 -> 2 -> 3
class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next = next

# For testing
def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> " if current.next else "")
        current = current.next
    print()

def shuffle_playlist(playlist):
    slow, fast = playlist, playlist

    while fast and fast.next:           # find the middle node
        slow = slow.next
        fast = fast.next.next

    curr = slow.next                    # the middle point is set as curr now, so if test case 1 curr is 3 -> 4
    slow.next = None                    # this set playlist is now only the first half

    prev = None
    while curr:                         # reversed the part after the middle node
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node
                                        # now prev is 4 -> 3

    p1 = playlist                       # p1 - the first half's pointer     / p2 - the second half's pointer
    p2 = prev

    while p2:                  # the merging MAGIC START HERE
        temp1 = p1.next             # save the next nodes so we don't lose the rest of the lists
        temp2 = p2.next

        p1.next = p2                # connect p1 to p2
        p2.next = temp1

        p1 = temp1                  # move pointers forward for the next iteration
        p2 = temp2
    return playlist

# Time Complexity - O(n) 
# Space Complexity O(1)
print("================ Problem 3 ====================")
playlist1 = Node(1, Node(2, Node(3, Node(4))))

playlist2 = Node(('Respect', 'Aretha Franklin'),
                Node(('Superstition', 'Stevie Wonder'),
                    Node(('Wonderwall', 'Oasis'),
                        Node(('Like a Prayer', 'Madonna'),
                            Node(('Bohemian Rhapsody', 'Queen'))))))

print_linked_list(shuffle_playlist(playlist1))
print_linked_list(shuffle_playlist(playlist2))



# ================ Problem 4 ====================
# Find the Intersection of two linked List
class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next = next

# For testing
def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> " if current.next else "")
        current = current.next
    print()

def playlist_overlap(playlist_a, playlist_b):
    a, b = playlist_a, playlist_b

    while a is not b:
        a = a.next if a else playlist_b
        b = b.next if b else playlist_a
    return a

# Time Complexity - O(n + m)
# Space Complexity - O(1)
print("================ Problem 4 ====================")
playlist_a = Node('Song A', Node('Song B'))
playlist_b = Node('Song X', Node('Song Y', Node('Song Z')))
shared_segment = Node('Song M', Node('Song N', Node('Song O')))

playlist_a.next.next = shared_segment
playlist_b.next.next.next = shared_segment

intersection = (playlist_overlap(playlist_a, playlist_b))

if intersection:
    print(intersection.value)
else:
    print(intersection)


# ================ Problem 5 ====================
class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next = next

# For testing
def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> " if current.next else "")
        current = current.next
    print()

def double_listeners(monthly_listeners):
    strg = ""
    curr = monthly_listeners

    while curr:
        strg += str(curr.value)
        curr = curr.next
    
    num = int(strg)

    double = str(num * 2)

    dummy = Node(0)
    curr = dummy
    for char in double:
        new_node = Node(char)
        curr.next = new_node
        curr = curr.next
    return dummy.next

# time complexity - O(n^2)
# space complexity - O(n)
print("================ Problem 5 ====================")
monthly_listeners1 = Node(1, Node(8, Node(9))) # 189
monthly_listeners2 = Node(9, Node(9, Node(9))) # 999

print_linked_list(double_listeners(monthly_listeners1))
print_linked_list(double_listeners(monthly_listeners2))