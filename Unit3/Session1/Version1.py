# ================ Problem 1 ====================
# P - append all char to stack []
#   - if char is the last index or the char is 'I'
#   - then add the entire stack to the result
#   - STACK : LIFO
def arrange_guest_arrival_order(arrival_pattern):
    stack = []
    res = []

    for i in range(len(arrival_pattern) + 1):
        stack.append(i + 1)

        if i == len(arrival_pattern) or arrival_pattern[i] == 'I':
            while stack:
                res.append(stack.pop())
    return ''.join(map(str, res))
        

print("================ Problem 1 ====================")
print(arrange_guest_arrival_order("IIIDIDDD"))  
print(arrange_guest_arrival_order("DDD"))  