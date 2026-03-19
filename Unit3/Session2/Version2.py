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
def match_buyers_and_sellers(buyers, sellers):
    sorted_buyers = sorted(buyers)
    sorted_sellers = sorted(sellers)
    count = 0
    
    for buy_price in sorted_buyers:
        i = 0
        while i < len(sorted_sellers):
            if buy_price >= sorted_sellers[i]:
                count += 1
                sorted_sellers.remove(sorted_sellers[i])
            else:
                i += 1
    return count


print("================ Problem 3 ====================")
buyers1 = [4, 7, 9]
sellers1 = [8, 2, 5, 8]
print(match_buyers_and_sellers(buyers1, sellers1)) 

buyers2 = [1, 1, 1]
sellers2 = [10]
print(match_buyers_and_sellers(buyers2, sellers2))



# ================ Problem 4 ====================
def maximum_value(items, x, y):
    # x = "ab"
    # y = "ba"
    larger = max(x, y)
    items_lst = list(items)
    i, j = 0, 1
    count_x, count_y = 0, 0
    if larger == y:
        while j < len(items_lst):
            if items_lst[i] == 'b' and items_lst[j] == 'a':
                count_y += 1
                items_lst.pop(i)
                items_lst.pop(j)
            else:
                i += 1
                j += 1
        
        if "ab" in "".join(items_lst):
            count_x += 1
    else:
        while j < len(items_lst):
            if items_lst[i] == 'a' and items_lst[j] == 'b':
                count_y += 1
                items_lst.pop(i)
                items_lst.pop(j)
            else:
                i += 1
                j += 1
        if "ba" in "".join(items_lst):
            count_x += 1
    return x*count_x + y*count_y
        
            

print("================ Problem 4 ====================")
s1 = "cdbcbbaaabab"
x1, y1 = 4, 5
print(maximum_value(s1, x1, y1))

s2 = "aabbaaxybbaabb"
x2, y2 = 5, 4
print(maximum_value(s2, x2, y2)) 