from collections import Counter
import string
# ================ Problem 1 ====================
def analyze_library(library_catalog, actual_distribution):
    res = {}
    for key, value in library_catalog.items():
        res[key] = actual_distribution[key] - value
    return res


print("================ Problem 1 ====================")
library_catalog = {
    "Room A": 150,
    "Room B": 200,
    "Room C": 250,
    "Room D": 300
}
actual_distribution = {
    "Room A": 150,
    "Room B": 190,
    "Room C": 260,
    "Room D": 300
}
print(analyze_library(library_catalog, actual_distribution))



# ================ Problem 2 ====================
def find_common_artifacts(artifacts1, artifacts2):
    common = set(artifacts1) & set(artifacts2)
    return list(common)


# alternative solution:
    # set1 = set(artifacts1)
    
    # Check the second list against the set without making a second set
    # The result list will be at most O(min(n, m))
    # return [item for item in artifacts2 if item in set1]

print("================ Problem 2 ====================")
artifacts1 = ["Statue of Zeus", "Golden Vase", "Bronze Shield"]
artifacts2 = ["Golden Vase", "Silver Sword", "Bronze Shield"]

print(find_common_artifacts(artifacts1, artifacts2))



# ================ Problem 3 ====================
def declutter(souvenirs, threshold):
    freq = Counter(souvenirs)
    res = []
    for key, value in freq.items():
        if value < threshold:
            res.append(key)
    return res


print("================ Problem 3 ====================")
souvenirs1 = ["coin", "alien egg", "coin", "coin", "map", "map", "statue"]
threshold1 = 3
print(declutter(souvenirs1, threshold1))

souvenirs2 = ["postcard", "postcard", "postcard", "sword"]
threshold2 = 2
print(declutter(souvenirs2, threshold2))



# ================ Problem 4 ====================
# ["777", "7", "77", "77"]
#          i
#    j    
def num_of_time_portals(portals, destination):
    i = 0
    res = 0
    while i < len(portals):
        for j in range (len(portals)):
            if j != i and portals[i] + portals[j] == destination:
                res += 1
        i += 1
    return res
        
print("================ Problem 4 ====================")
portals1 = ["777", "7", "77", "77"]
destination1 = "7777"
portals2 = ["123", "4", "12", "34"]
destination2 = "1234"
portals3 = ["1", "1", "1"]
destination3 = "11"

print(num_of_time_portals(portals1, destination1))
print(num_of_time_portals(portals2, destination2))
print(num_of_time_portals(portals3, destination3))




# ================ Problem 5 ====================
# U - the list is the door number, if the door are the same number
#   - the difference btw need to be smaller than the k
#   - test case 1: [1, 2, 3, 1], 1 exist two times in index[0] and index[4]
#   - difference is 3, not more than k, so its True
# P - use 2 pointers, set i = 0, j = 1
#   - if j value != i value, j increment, otherwise if i == 0, i+=1; j-i
#   - check is j-i larger than k, return boolean
def detect_temporal_anomaly(time_points, k):
    gap = []
    i, j = 0, 1
    difference = 0
    while j < len(time_points):
        if time_points[i] != time_points[j]:
            j += 1
        else:
            if i == 0:
               i += 1
            difference = j - i
            gap.append(difference)
            i += 1
            j = i + 1
    return max(gap) <= k 


print("================ Problem 5 ====================")
time_points1 = [1, 2, 3, 1]
k1 = 3

time_points2 = [1, 0, 1, 1]
k2 = 1

time_points3 = [1, 2, 3, 1, 2, 3]
k3 = 2

print(detect_temporal_anomaly(time_points1, k1))  
print(detect_temporal_anomaly(time_points2, k2)) 
print(detect_temporal_anomaly(time_points3, k3)) 



# ================ Problem 6 ====================
# U - each item in the races list, item[0] - the winner, item[1] is lost ONE time only
#   - return a list with two element, 2nd element: all items[1] that only have one freq(unique)
#   - 1st element: all items[0] not include the 2nd element list
# P - use Counter, {1:1, 2:1, 3:2, 4:3, 5:2, ...} {key=number, value=# of times exist}
#   - set empty res = [], res[1] =  loop and append any key has the freq value == 1
#   - res[0] = (loop through races, append in a [] for all of the index 0 number) use XOR with res[1]
def find_travelers(races):
    loser = [item[1] for item in races]
    freq_lost = Counter(loser)
    lost_one = []
    for key, value in freq_lost.items():
        if value == 1:
            lost_one.append(key)
    win_lost = [item[0] for item in races]  
    winner = set([num for num in win_lost if num not in loser])   
    return [list(winner), lost_one]


print("================ Problem 6 ====================")
races1 = [[1, 3], [2, 3], [3, 6], [5, 6], [5, 7], [4, 5], [4, 8], [4, 9], [10, 4], [10, 9]]
races2 = [[2, 3], [1, 3], [5, 4], [6, 4]]

print(find_travelers(races1))  
print(find_travelers(races2)) 


# ================ Problem 7 ====================
# U - putuation is not counted, space is not counted, the word in illegivle list is not counted
#   - find the most feq word/substring
# P - convert para into a list, spilt by - not alpha()/ it is a space
#   - convert everything to lowercase, use Counter to get the freq dict
#   - find the max freq, and check the word(key) is not in illegibles list
def find_most_frequent_word(text, illegibles):
    text_lst = "".join(char.lower() for char in text if char not in string.punctuation)
    clean_text = text_lst.split(" ")
    freq = Counter(clean_text)
    res = []
    for illegible in illegibles:
        if illegible in freq:
            freq.pop(illegible)
    highest = max(freq.values())        
    for key, value in freq.items():
        if value == highest:
            res.append(key)
    return res
        

print("================ Problem 7 ====================")
paragraph1 = "a."
illegibles1 = []
print(find_most_frequent_word(paragraph1, illegibles1)) 

paragraph2 = "Bob hit a ball, the hit BALL flew far after it was hit."
illegibles2 = ["hit"]
print(find_most_frequent_word(paragraph2, illegibles2)) 


# ================ Problem 8 ====================
# ['Portal','10:00','10:15','10:30','11:00']
# [   '3',    '2',    '0',    '1',    '0'  ]
# [   '5',    '1',    '0',    '0',    '1'  ]
# [  '10',    '0',    '1',    '0',    '0'  ]
# P - res[0] = 'Portal', the unique ( loop thru useage_records, each element[2] ) <- SORT > SET > append
#   - append to res (set( loop thre uage_records, each element[1])) <- SORT
#   - try to build a structure like { "3": {"10:00": 2, "10:30": 1}, "5": {"10:00": 1, "11:00": 1}, ...}
#   - then allocate to the list (sort by time)
def display_time_portal_usage(usage_records):
    res = [['Portal']]
    time = sorted(set([(item[2]) for item in usage_records]))
    for t in time:
        res[0].append(t)
    portal_num = sorted(set([item[1] for item in usage_records]), key=int)

    for num in portal_num:
        res.append([num])

    time_portals = {}
    for item in usage_records:
        if item[1] not in time_portals:
            time_portals[item[1]] = {item[2] : 1}
        else:
            if item[2] not in time_portals[item[1]]:
                time_portals[item[1]][item[2]] = 1
            else:
                time_portals[item[1]][item[2]] += 1

    for i in range (1, len(res)):
        portal = res[i][0]
        for t in time:
            count = time_portals[portal].get(t, 0)
            res[i].append(str(count))
            
    return res
    

print("================ Problem 8 ====================")
usage_records1 = [["David","3","10:00"],
                  ["Corina","10","10:15"],
                  ["David","3","10:30"],
                  ["Carla","5","11:00"],
                  ["Carla","5","10:00"],
                  ["Rous","3","10:00"]]
usage_records2 = [["James","12","11:00"],
                  ["Ratesh","12","11:00"],
                  ["Amadeus","12","11:00"],
                  ["Adam","1","09:00"],
                  ["Brianna","1","09:00"]]
usage_records3 = [["Laura","2","08:00"],
                  ["Jhon","2","08:15"],
                  ["Melissa","2","08:30"]]

print(display_time_portal_usage(usage_records1))
print(display_time_portal_usage(usage_records2))
print(display_time_portal_usage(usage_records3))