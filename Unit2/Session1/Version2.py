from collections import Counter
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
def detect_temporal_anomaly(time_points, k):



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
