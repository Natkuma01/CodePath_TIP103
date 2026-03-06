# ============ problem 1 ============
# matrix1[0][0] + matrix2[0][0]
# matrix1[0][1] + matrix2[0][1]
# matrix1[0][2] + matrix2[0][2]
# matrix1[1][0] + matrix2[1][0]

def add_matrices(matrix1, matrix2):
    sum_matrix = []
    for i in range (len(matrix1)):
        temp = []
        for j in range (len(matrix1)):
            temp.append(matrix1[i][j] + matrix2[i][j])
        sum_matrix.append(temp)
    return sum_matrix

print("============ problem 1 ===========")
matrix1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matrix2 = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
]

print(add_matrices(matrix1, matrix2))


# ============ problem 2 ============
def is_palindrome(s):
    i, j = 0, len(s)-1
    while i < j:
        if s[i] == s[j]:
            i += 1
            j -= 1
        else:
            return False
    return True

print("============ problem 2 ===========")
s = "madam"
print(is_palindrome(s))

s = "madamweb"
print(is_palindrome(s))



# ============ problem 3 ============
# split it -> become a list
# loop through and strip each item
# join them back with space
def squash_spaces(s):
    new_lst = s.split()
    for item in new_lst:
        item = item.strip()
    return (" ").join(new_lst)   

print("============ problem 3 ===========")
s = "   Up,     up,   and  away! "
print(squash_spaces(s))

s = "With great power comes great responsibility."
print(squash_spaces(s))


# ============ problem 4 ============
# loop through if (target - num) is in the list
# return the index, use enumerate
# seen = {number: index}
def two_sum(nums, target):
    seen = {}
    for index, num in enumerate(nums):
        looking = target - num
        if looking in seen:
            return [seen[looking], index]
        else:
            seen[num] = index

print("============ problem 4 ===========")
nums = [2, 7, 11, 15]
target = 9
print(two_sum(nums, target))

nums = [2, 7, 11, 15]
target = 18
print(two_sum(nums, target))


# ============ problem 5 ============
# sorted the nums list
# set empty list to append the result
# use enumerate to loop through
# check and make sure i is not 0, and not duplicate
# set left to index 1, right to last index
# add up the current num, left, right 
# if its 0, append, if less than 0, add a bigger number
# else add a smaller number
def three_sum(nums):
    nums.sort()
    res = []
    for i, num in enumerate(nums):
        if i > 0 and num == nums[i-1]:
            continue
        left, right = i+1, len(nums)-1

        while left < right:
            total = num + nums[left] + nums[right]
            if total == 0:
                res.append([num, nums[left], nums[right]])
                left += 1
                while left < right and nums[left] == nums[left-1]:
                    left += 1
            elif total < 0:
                left += 1
            else:
                right -= 1
    return res
            
        


print("============ problem 5 ===========")
nums = [-1, 0, 1, 2, -1, -4]
print(three_sum(nums))

nums = [0, 1, 1]
print(three_sum(nums))

nums = [0, 0, 0]
print(three_sum(nums))
