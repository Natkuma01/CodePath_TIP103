# ================ Problem 1 ====================
def count_layers(sandwich):
    if not sandwich:            # base case
        return 0
    if len(sandwich) == 1:      # base case
        return 1
    return 1 + count_layers(sandwich[1])

print("================ Problem 1 ====================")
sandwich1 = ["bread", ["lettuce", ["tomato", ["bread"]]]]
sandwich2 = ["bread", ["cheese", ["ham", ["mustard", ["bread"]]]]]

print(count_layers(sandwich1))
print(count_layers(sandwich2))


# ================ Problem 2 ====================
def reverse_helpers(items):
    if len(items) == 1:
        return items[0]
    return reverse_helpers(items[1:]) + " " + items[0]

def reverse_orders(orders):
    items = orders.split()
    return reverse_helpers(items)

print("================ Problem 2 ====================")
print(reverse_orders("Bagel Sandwich Coffee"))



# ================ Problem 3 ====================
def add_coffee(bags):
    if len(bags) == 1:
        return bags[0]
    return bags[0] + add_coffee(bags[1:])

def can_split_coffee(coffee, n):
    return add_coffee(coffee) % n == 0

print("================ Problem 3 ====================")
print(can_split_coffee([4, 4, 8], 2))
print(can_split_coffee([5, 10, 15], 4))



# ================ Problem 4 ====================
# linkedlist merging + recursion
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

def merge_orders(sandwich_a, sandwich_b):    
    if sandwich_a is None:
        return sandwich_b
    if sandwich_b is None:
        return sandwich_a
    
    next_a = sandwich_a.next
    next_b = sandwich_a.next

    sandwich_a.next = sandwich_b
    sandwich_b.next = merge_orders(next_a, next_b)

    return sandwich_a

print("================ Problem 4 ====================")
sandwich_a = Node('Bacon', Node('Lettuce', Node('Tomato')))
sandwich_b = Node('Turkey', Node('Cheese', Node('Mayo')))
sandwich_c = Node('Bread')

print_linked_list(merge_orders(sandwich_a, sandwich_b))
# print_linked_list(merge_orders(sandwich_a, sandwich_c))



# ================ Problem 6 ====================
def evaluate_ternary_expression_iterative(expression):
    stack = []
    
    # Traverse the expression from right to left
    for i in range(len(expression) - 1, -1, -1):
        char = expression[i]
        
        if stack and stack[-1] == '?':
            stack.pop()  # Remove the '?'
            true_expr = stack.pop()  # True expression
            stack.pop()  # Remove the ':'
            false_expr = stack.pop()  # False expression
            
            if char == 'T':
                stack.append(true_expr)
            else:
                stack.append(false_expr)
        else:
            stack.append(char)
    
    return stack[0]

def evaluate_ternary_expression_recursive(expression):
    pass

print("================ Problem 6 ====================")
print(evaluate_ternary_expression_recursive("T?2:3"))
print(evaluate_ternary_expression_recursive("F?1:T?4:5"))
print(evaluate_ternary_expression_recursive("T?T?F:5:3"))