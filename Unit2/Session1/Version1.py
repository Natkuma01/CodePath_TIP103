# ================ Problem 1 ====================
def total_treasures(treasure_map):
    total = 0
    for key, item in treasure_map.items():
        total += item
    return total

treasure_map1 = {
    "Cove": 3,
    "Beach": 7,
    "Forest": 5
}

treasure_map2 = {
    "Shipwreck": 10,
    "Cave": 20,
    "Lagoon": 15,
    "Island Peak": 5
}
print("================ Problem 1 ====================")
print(total_treasures(treasure_map1)) 
print(total_treasures(treasure_map2)) 


# ================ Problem 2 ====================
def can_trust_message(message):
    all_alp = {}
    for char in message:
        if char in all_alp:
            continue
        else:
            all_alp[char] = 1
    return len(all_alp) == 26 or len(all_alp) == 27


message1 = "sphinx of black quartz judge my vow"
message2 = "trust me"
print("================ Problem 2 ====================")
print(can_trust_message(message1))
print(can_trust_message(message2))


# ================ Problem 3 ====================
def find_duplicate_chests(chests):
    freq = {}
    duplicate = []
    for num in chests:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1
    for key, item in freq.items():
        if item > 1:
            duplicate.append(key)
    return duplicate

chests1 = [4, 3, 2, 7, 8, 2, 3, 1]
chests2 = [1, 1, 2]
chests3 = [1]

print("================ Problem 3 ====================")
print(find_duplicate_chests(chests1))
print(find_duplicate_chests(chests2))
print(find_duplicate_chests(chests3))


# ================ Problem 4 ====================
def can_make_balanced(code):
    freq = {}
    for num in code:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1
    biggest = max(freq.values())
    count = 0
    for num in freq.values():
        if num == biggest - 1:
            count += 1
    return count == len(freq) - 1

code1 = "arghh"
code2 = "haha"
print("================ Problem 4 ====================")
print(can_make_balanced(code1)) 
print(can_make_balanced(code2)) 


# ================ Problem 5 ====================
def find_treasure_indices(gold_amounts, target):
    ref = {}
    for i in range (len(gold_amounts)):
        if target - gold_amounts[i] in ref:
            return [i, ref[target-gold_amounts[i]]]
        else:
            ref[gold_amounts[i]] = i

print("================ Problem 5 ====================")
gold_amounts1 = [2, 7, 11, 15]
target1 = 9

gold_amounts2 = [3, 2, 4]
target2 = 6

gold_amounts3 = [3, 3]
target3 = 6

print(find_treasure_indices(gold_amounts1, target1))  
print(find_treasure_indices(gold_amounts2, target2))  
print(find_treasure_indices(gold_amounts3, target3)) 


# ================ Problem 6 ====================
# dict = {3:[0, 1, 2, 3, 4, 6], 1:[5]}
# count = dict[0] list len / key
# while count > 0:
# loop through the dict[0] use range (key):
# temp = [0, 1, 2]
# append temp, reset temp
# count -= 1
def organize_pirate_crew(group_sizes):
    ref = {}
    for i, num in enumerate(group_sizes):
        if num not in ref:
            ref[num] = [i]
        else:
            value_list = ref[num]
            value_list.append(i)
            res = []
    for key, value in ref.items():
        count = len(value) / key
        while count > 0:
            temp = []
            for i in range (key):
                temp.append(value[i])
            count -= 1
            res.append(temp)
            value = value[key:]
    return res
    

group_sizes1 = [3, 3, 3, 3, 3, 1, 3]
group_sizes2 = [2, 1, 3, 3, 3, 2]
print("================ Problem 6 ====================")
print(organize_pirate_crew(group_sizes1))
print(organize_pirate_crew(group_sizes2)) 



# ================ Problem 7 ====================
# iterate the char in map1
# convert map2 to a list
# if that char is in map2, remove the char
# return the lengtht of the list map2
def min_steps_to_match_maps(map1, map2):
    lst_map2 = list(map2)
    for char in map1:
        if char in lst_map2:
            lst_map2.remove(char)
    return len(lst_map2)


print("================ Problem 7 ====================")
map1_1 = "bab"
map2_1 = "aba"
map1_2 = "treasure"
map2_2 = "huntgold"
map1_3 = "anagram"
map2_3 = "mangaar"

print(min_steps_to_match_maps(map1_1, map2_1))
print(min_steps_to_match_maps(map1_2, map2_2))
print(min_steps_to_match_maps(map1_3, map2_3))




# ================ Problem 8 ====================
# U - the logs [0, 5] ==> pirate#0 acted at 5 min
#   - that is 1 unique PAM (pirate action minute)
#   - return the result [#pirates have 1 unique PAM, #pirate have 2 unique PAM, .....]
#   - k is the length of the result
# P - set up empty dict
#   - loop through logs
#   - if item[0] not in the dict, set item[0] as the key of dict, item[1] is the value (a list)
#   - else append the value into the same key
#   - create the answer = [] 0*k
#   - for value in the dict, get the dict value len
#   - answer[len_value] = 1 (if answer[len_value] == 0)
#   - otherwise answer[len_value] += 1, return the answer list
def counting_pirates_action_minutes(logs, k):
    action_min = {}
    for item in logs:
        if item[0] not in action_min:
            action_min[item[0]] = [item[1]]
        else:
            action_min[item[0]].append(item[1])
    answer = [0] * k
    for value in action_min.values():
        value = set(value)
        answer[len(value)-1] += 1
    return answer


print("================ Problem 8 ====================")
logs1 = [[0, 5], [1, 2], [0, 2], [0, 5], [1, 3]]
k1 = 5
logs2 = [[1, 1], [2, 2], [2, 3]]
k2 = 4

print(counting_pirates_action_minutes(logs1, k1)) 
print(counting_pirates_action_minutes(logs2, k2))
