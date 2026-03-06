# ================= Problem 1 =================
def linear_search(items, target):
    if target not in items:
        return -1
    for i in range (len(items)):
        if items[i] == target:
            return i

print("=========== Problem 1 ===============")
items = ['haycorn', 'haycorn', 'haycorn', 'hunny', 'haycorn']
target = 'hunny'
print(linear_search(items, target))

items = ['bed', 'blue jacket', 'red shirt', 'hunny']
target = 'red balloon'
print(linear_search(items, target))


# ================= Problem 2 =================
# set up variable tigger = 1
# loop through the operations list
# if the element in operations list == bouncy or == flouncy
# tigger increment
# otherwise tigger decrement
# return tigger

def final_value_after_operations(operations):
    tigger = 1
    for item in operations:
        if item == "bouncy" or item == "flouncy":
            tigger += 1
        else:
            tigger -= 1
    return tigger

print("=========== Problem 2 ===============")
operations = ["trouncy", "flouncy", "flouncy"]
print(final_value_after_operations(operations))

operations = ["bouncy", "bouncy", "flouncy"]
print(final_value_after_operations(operations))

# ================= Problem 3 =================
# set a list with all the substrings that need to remove
# set an empty string s
# if the letter is not those substring, add on the empty string

def tiggerfy(word):
    remove_string = ['gg', 'er', 't', 'i']
    
    res = word.lower()
    for sub in remove_string:
        res = res.replace(sub, "")
    return res
    

print("=========== Problem 3 ===============")
word = "Trigger"
print(tiggerfy(word))

word = "eggplant"
print(tiggerfy(word))

word = "Choir"
print(tiggerfy(word))

# ================= Problem 4 =================
# index 0 has to be the smallest number, index 2 has to be the largest number


def non_decreasing(nums):
    violation = 0

    for i in range (len(nums)-1):
        if nums[i] > nums[i+1]:
            violation += 1
            if violation > 1:
                return False
    return True

print("=========== Problem 4 ===============")
nums = [4, 2, 3]
print(non_decreasing(nums))

nums = [4, 2, 1]
print(non_decreasing(nums))

# ================= Problem 5 =================
# check if length of clues is less than / equal to 1, if yes, return []
# res = []
# loop through the list clues
# temp = []
# if clues[i+1] - clues[i] > 1, append clues[i] + 1 in a temp, and append clues[i+1] - 1 in the temp
# reset temp
# if the last index is not equal to the upper
# add [ the clues[-1] - 1, upper]


def find_missing_clues(clues, lower, upper):
    if len(clues) <= 1:
        return []
    res = []
    for i in range (len(clues)-1):
        if clues[i+1] - clues[i] > 1:
            res.append([clues[i] + 1, clues[i+1] - 1])

    if clues[-1] < upper:
        res.append([clues[-1] + 1, upper])

    return res

print("=========== Problem 5 ===============")
clues = [0, 1, 3, 50, 75]
lower = 0
upper = 99
print(find_missing_clues(clues, lower, upper))

clues = [-1]
lower = -1
upper = -1
print(find_missing_clues(clues, lower, upper))


# ================= Problem 6 =================



print("=========== Problem 6 ===============")



# ================= Problem 7 =================



print("=========== Problem 7 ===============")


# ================= Problem 8 =================



print("=========== Problem 8 ===============")

