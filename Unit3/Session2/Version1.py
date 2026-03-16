from collections import deque
# ================ Problem 1 ====================
# U - sorting with queue
# P - put blueprints in a deque, created the approved empty list
#   - when the deque still has items, find the smallest element
#   - loop through the deque, if the smallest element == element in deque
#   - append to the approved empty list, otherwise add to the back of the deque
def blueprint_approval(blueprints):
    q = deque(blueprints)

    res = []

    while q:
        smallest = min(q)
        for _ in range (len(q)):
            num = q.popleft()
            if num == smallest:
                res.append(num)
            else:
                q.append(num)
    return res


print("================ Problem 1 ====================")
print(blueprint_approval([3, 5, 2, 1, 4])) 
print(blueprint_approval([7, 4, 6, 2, 5])) 



# ================ Problem 2 ====================
# P - two pointer, i, j / if j less than i, count += 1
def build_skyscrapers(floors):
    i, j = 0, 1
    count = 1
    while j < len(floors):
        if floors[j] > floors[i]:
            count += 1
        i += 1
        j += 1
    return count



print("================ Problem 2 ====================")
print(build_skyscrapers([10, 5, 8, 3, 7, 2, 9])) 
print(build_skyscrapers([7, 3, 7, 3, 5, 1, 6]))  
print(build_skyscrapers([8, 6, 4, 7, 5, 3, 2])) 
# 8, 6, 4, 7, 5, 3, 2
#          i
#                j


# ================ Problem 3 ====================
def max_corridor_area(segments):
    i, j = 0, len(segments)-1

    areas = []

    while j > i:
        while i < j:
            distance = j - i
            min_num = min(segments[i], segments[j])
            areas.append(min_num * distance)
            i += 1
        j -= 1
    return max(areas)


print("================ Problem 3 ====================")
print(max_corridor_area([1, 8, 6, 2, 5, 4, 8, 3, 7])) 
print(max_corridor_area([1, 1])) 

# Alternative solution for Problem 3
# -----------------------------------
# def max_corridor_area(segments):
#     i, j = 0, len(segments)-1
#     areas = []

#     while i < j:
#         distance = j - i
#         min_num = min(segments[i], segments[j])
#         areas.append(min_num * distance)
#         if segments[i] < segments[j]:
#             i += 1
#         else:
#             j -= 1

#     return max(areas)



# ================ Problem 4 ====================
# P - one swap fix 2 imbalance
#   - find out how many swap need, and divided by 2 (//)
def min_swaps(s):
    imbalance = 0
    max_imbalance = 0

    for char in s:
        if char =='[':
            imbalance -= 1
        else:
            imbalance += 1
        max_imbalance = max(max_imbalance, imbalance)

    return (max_imbalance + 1) // 2


print("================ Problem 4 ====================")
print(min_swaps("][][")) 
print(min_swaps("]]][[[")) 
print(min_swaps("[]"))  


# ================ Problem 5 ====================
# U - cannot remove any letters, make the string become balance/ valid
# P - loop through the string, if the string is '(' , append to deque
#   - if string is ')', append in dictionary(may need to remove)
def make_balanced_room(s):
    q = deque()
    s_list = list(s)

    for i, v in enumerate(s):
        if v == '(':
            q.append([i, v])
        elif v == ')':
            if q and q[-1][1] == '(':
                q.pop()
            else:
                q.append([i, v])
    
    remove_index = []
    for item in q:
        remove_index.append(item[0])

    remove_index.sort(reverse=True)
    
    for indx in remove_index:
        s_list.pop(indx)
    
    return "".join(s_list)
        

print("================ Problem 5 ====================")
print(make_balanced_room("art(t(d)e)sign)")) 
print(make_balanced_room("d)e(s)ign")) 
print(make_balanced_room("))((")) 



# ================ Problem 6 ====================
# U - subtract the index if the value of i+1 > the value of i
#   - the last num is always 0
# P - use enumerate
def time_to_complete_dream_designs(design_times):
    res = [0] * len(design_times)
    stack = []
    for i, value in enumerate(design_times):
        while stack and design_times[i] > design_times[stack[-1]]:
            prev_indx = stack.pop()
            res[prev_indx] = i - prev_indx
        stack.append(i)  
    return res  


print("================ Problem 6 ====================")
print(time_to_complete_dream_designs([3, 4, 5, 2, 1, 6, 7, 3])) 
print(time_to_complete_dream_designs([2, 3, 1, 4]))  
print(time_to_complete_dream_designs([5, 5, 5, 5])) 



# ================ Problem 7 ====================
def next_greater_dream(dreams):
    res = [-1] * len(dreams)
    stack = []
    seen = {}

    for i in range (len(dreams)):
        if stack and dreams[i] > dreams[stack[-1]]:
            seen[dreams[stack[-1]]] = dreams[i]
            prev_indx = stack.pop()
            res[prev_indx] = dreams[i]
        elif dreams[i] in seen:
            res[i] = seen[dreams[i]]
            
        stack.append(i)
    return res  


print("================ Problem 7 ====================")
print(next_greater_dream([1, 2, 1])) 
print(next_greater_dream([1, 2, 3, 4, 3])) 


# if largest -> -1
# 