import heapq
from collections import deque
# ================ Problem 1 ====================
def predictAdoption_victory(votes):
    if votes.count('C') > votes.count('D'):
        return "Cats Lover"
    elif votes.count('D') > votes.count('C'):
        return "Dogs Lover"
    else:
        if votes.index('C') < votes.index('D'):
            return "Cats Lover"
        else: 
            return "Dogs Lover"
print("================ Problem 1 ====================")
print(predictAdoption_victory("CD")) 
print(predictAdoption_victory("CDD")) 



# ================ Problem 2 ====================
# U - find the smallest max number
# P - use two pointer
#   - l : index 0  r : last index
#   - sort the list
#   - compare each l + r see which one is the max
def pair_up_animals(discomfort_levels):
    l, r = 0, len(discomfort_levels)-1

    discomfort_levels.sort()

    smallest_max = 0
    while l < r:
        pair_sum = discomfort_levels[l] + discomfort_levels[r]
        smallest_max = max(smallest_max, pair_sum)
        l += 1
        r -= 1
    return smallest_max
    

print("================ Problem 2 ====================")
print(pair_up_animals([3,5,2,3]))  
print(pair_up_animals([3,5,4,2,4,6])) 



# ================ Problem 3 ====================
# U - Stack : LIFO
#   - stac --> cats     lovecats --> stacevol   !stacevolI --> Ilovecats!
#   - only flip the words that inside the ()
# P - push all char from s, ')' --> pop until '('
#   - put back the word into the stack
def rearrange_animal_names(s):
    stack = []

    for char in s:
        temp = ""
        if char == ')':
            while stack and stack[-1] != '(':
                temp += stack.pop()
            stack.pop()
            
            for c in temp:
                stack.append(c)
        else:
            stack.append(char)

    return "".join(stack)


print("================ Problem 3 ====================")
print(rearrange_animal_names("(dribtacgod)"))
print(rearrange_animal_names("(!(love(stac))I)")) 
print(rearrange_animal_names("adopt(yadot(a(tep)))!")) 



# ================ Problem 4 ====================
def append_animals(available, preferred):

    i, j = 0, 0
    count = 0

    while i < len(available) and j < len(preferred):
        if available[i] == preferred[j]:
            i += 1
            j += 1
            count += 1
        else:
            i += 1
    return len(preferred) - count


print("================ Problem 4 ====================")
print(append_animals("catsdogs", "cows")) 
print(append_animals("rabbit", "r")) 
print(append_animals("fish", "bird"))



# ================ Problem 5 ====================
# U - grouping all letter, Ex. a can be in group one, cannot be in group 2
#   - Ex. ababcbaca / defegde / hijhklij - [9, 7, 8]
# P - make dictionary to find all last index of each char
#   - see the current index it the largest number
#   - set the largest to "end", and if the current index == end, 
#   - append the (end - start) + 1 to an empty list 
#   - start = i + 1
def group_animals_by_habitat(habitats):
    last_index = {}

    for i, value in enumerate(habitats):
        last_index[value] = i
    
    res = []
    start, end = 0, 0

    for i, value in enumerate(habitats):
        end = max(end, last_index[value])
        if i == end:
            res.append(end-start + 1)
            start = i + 1
    return res
   

print("================ Problem 5 ====================")
print(group_animals_by_habitat("ababcbacadefegdehijhklij")) 
print(group_animals_by_habitat("eccbbbbdec"))


# ================ Problem 6 ====================
# U - adopt has to be in order
# P - Stack
#   - create a stack, keep put element in, then check the last num in the stack == first num in adopted?
#   - if yes? pop stack, check the next num in adopt
#   - if no, check the rest of the list, if in the list, keep stack the next element
#   - if the list empty, return false
def validate_shelter_sequence(admitted, adopted):
    stack = []

    i, j = 0, 0
    while i < len(admitted):
        stack.append(admitted[i])
        i += 1
        while j < len(adopted) and stack[-1] == adopted[j]:
            stack.pop()
            j += 1
    
    return not stack
                

print("================ Problem 6 ====================")
print(validate_shelter_sequence([1,2,3,4,5], [4,5,3,2,1]))
print(validate_shelter_sequence([1,2,3,4,5], [4,3,5,1,2])) 