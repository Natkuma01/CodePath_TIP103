# ================ Problem 1 ====================
def score_of_mystical_market_chains(chain):
    stack = []
    count = 0

    for char in chain:
        if char == '(':
            stack.append(char)
        elif stack and char == ')':
            stack.pop()
            count += 1
    return count

print("================ Problem 1 ====================")
print(score_of_mystical_market_chains("()"))  
print(score_of_mystical_market_chains("(())"))
print(score_of_mystical_market_chains("()()")) 



# ================ Problem 2 ====================
def arrange_magical_orbs(orbs):
    left, curr, right = 0, 1, 2

    while right < len(orbs):
        if orbs[left] > orbs[right]:
            orbs[right], orbs[left] = orbs[left], orbs[right]
            left += 1
            right += 1
        elif orbs[left] <=  orbs[right]:
            right += 1
    return orbs



print("================ Problem 2 ====================")
orbs1 = [2, 0, 2, 1, 1, 0]
arrange_magical_orbs(orbs1)
print(orbs1) 

orbs2 = [2, 0, 1]
arrange_magical_orbs(orbs2)
print(orbs2) 


# ================ Problem 3 ====================


print("================ Problem 3 ====================")





# ==================
def rotate_matrix(matrix):
    res = []
    for i in range (len(matrix)):
        temp = []
        for j in range(len(matrix[0])):
            temp.append(matrix[j][i])
        res.append(temp[::-1])
    return res

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(rotate_matrix(matrix))
# 20 10 00
# 21 11 01
# 22 12 02