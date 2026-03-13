from collections import deque
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


# ================ Problem 2 ====================
# U - sort the input
#   - [2, 3, 5, 7, 11, 13, 17]: add 17 to [], add 13 before 17, bring the last index to the front
#   - [17]  -> [13, 17]  -> [17, 13]  -> [11, 17, 13]  -> [13, 11, 17]
def reveal_attendee_list_in_order(attendees):
    sorted_attendees = sorted(attendees)
    rev = sorted_attendees[::-1]
    q = deque([rev[0]])

    for i in range (1, len(attendees)):
        q.appendleft(rev[i])
        last_num = q.pop()
        q.appendleft(last_num)
    
    num = q.popleft()
    q.append(num)

    return q


print("================ Problem 2 ====================")
print(reveal_attendee_list_in_order([17,13,11,2,3,5,7])) 
print(reveal_attendee_list_in_order([1,1000])) 



# ================ Problem 3 ====================
# P - use three pointers
#   - left, right, current
#   - if current less than priority, current switch with left
#   - if current greater than prority, current switch with right
#   - if current == priority, current move forward
def arrange_attendees_by_priority(attendees, priority):
    l, curr, r = 0, 0, len(attendees)-1

    while curr < r:
        if attendees[curr] < priority:
            attendees[l], attendees[curr] = attendees[curr], attendees[l]
            curr += 1
            l += 1
        elif attendees[curr] == priority:
             curr += 1
        else:
            attendees[curr], attendees[r] = attendees[r], attendees[curr]
            r -= 1
    return attendees
        

print("================ Problem 3 ====================")
print(arrange_attendees_by_priority([9,12,5,10,14,3,10], 10)) 
print(arrange_attendees_by_priority([-3,4,3,2], 2)) 


# ================ Problem 4 ====================
def rearrange_guests(guests):
    i, j = 0, 0
    while j < len(guests):
        if guests[i] > 0:
            j += 1
        elif guests[i] < 0:
            guests[i], guests[j] = guests[j], guests[i]
            i += 1
        elif guests[j] > 0:
             i += 1
        elif guests[j] < 0:
             i += 2
    return guests

print("================ Problem 4 ====================")
print(rearrange_guests([3,1,-2,-5,2,-4]))  
print(rearrange_guests([-1,1])) 

# [3, -2, 1, -5, 2, -4]               if i positive, j move, if j is positive i move if j is neg i+=2
#                     i
#                 j



# ================ Problem 5 ====================
# P - if its open, append to empty, if its close, pop the open
#   - count the len in the deque
def min_changes_to_make_balanced(schedule):
    validate = deque([])
    count = 0

    for parenthesis in schedule:
        if parenthesis == '(':
            validate.append(parenthesis)
        else:
            if validate:
                validate.pop()
            else:
                count += 1
    return len(validate) + count
    


print("================ Problem 5 ====================")
print(min_changes_to_make_balanced("())"))
print(min_changes_to_make_balanced("(((")) 



# ================ Problem 6 ====================

#   "abca", "aabcaca"
#            ???????
#            abca???
#            abcabca
#            aabcaca



print("================ Problem 6 ====================")
