# ============ problem 1 ===========
original = [[2, 4, -1],
            [-10, 5, 11],
            [18, -7, 6]
            ]

fliped = [[2, -10, 18],
         [4, 5, -7],
         [-1, 11, 6]
        ]

# set new list to insert the row
# take the columns from the original, make it to the list, insert to the new list

# [0][0] , [1][0], [2][0] ==> make list
# [0][1] , [1][1], [2][1]
# [j][i]
def transpose(matrix):
    res = []
    for i in range (len(matrix[0])):
        thershold = []
        for j in range (len(matrix)):
            thershold.append(matrix[j][i])
        res.append(thershold)
    return res


matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(transpose(matrix))

matrix = [
    [1, 2, 3],
    [4, 5, 6]
]
print(transpose(matrix))

# ============ problem 2 ===========
# set i index 0 to start, j can be the last index on the list
# swap i and j
def reverse_list(lst):
    i, j = 0, len(lst)-1
    while i < j:
        lst[i], lst[j] = lst[j], lst[i]
        i += 1
        j-= 1
    return lst

lst = ["pooh", "christopher robin", "piglet", "roo", "eeyore"]
print(reverse_list(lst))

# ============ problem 3 ===========
def remove_dupes(items):
    count = 0
    for i in range (len(items)-1):
        if items[i] == items[i+1]:
            count += 1
    return len(items) - count
        
print("============ problem 3 ===========")
items = ["extract of malt", "haycorns", "honey", "thistle", "thistle"]
print(remove_dupes(items))

items = ["extract of malt", "haycorns", "honey", "thistle"]
print(remove_dupes(items))


# ============ problem 4 ===========
# create a new list
# take out items in the nums list, if its even insert at the beginning, if odd insert at the end
def sort_by_parity(nums):
    res = []
    for num in nums:
        if num % 2 == 0:
            res.insert(0, num)
        else:
            res.insert(-1, num)
    return res

print("============ problem 4 ===========")
nums = [3, 1, 2, 4]
print(sort_by_parity(nums))

nums = [0]
print(sort_by_parity(nums))


# ============ problem 6 ===========
# loop through the interval list. -> for item in interval
# if the second element in the first item is larger than the first element in the next item
# get the first element in the first item and the second element in the next item
def merge_intervals(intervals):
    res = []
    i = 0
    while i < len(intervals):
        item = intervals[i]
        if i != len(intervals)-1:
            next_item = intervals[i+1]
            if item[1] >= next_item[0]:
                res.append([item[0], next_item[1]])
                i += 2
            else: 
                res.append([item[0], item[1]])
                i += 1
        else:
            res.append([item[0], item[1]])
            i += 1
    return res

print("============ problem 6 ===========")
intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
print(merge_intervals(intervals))

intervals = [[1, 4], [4, 5]]
print(merge_intervals(intervals))
