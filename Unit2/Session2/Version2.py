from collections import Counter
# ================ Problem 1 ====================
def max_attempts(ingredients, target_meal):
    ingredients_dict = Counter(ingredients)

    new_dict = {}
    for char in target_meal:
        if char in ingredients_dict:
            new_dict[char] = ingredients_dict[char]
    
    count = min(new_dict.values())

    return count

print("================ Problem 1 ====================")
ingredients1 = "aabbbcccc"
target_meal1 = "abc"
print(max_attempts(ingredients1, target_meal1))

ingredients2 = "ppppqqqrrr"
target_meal2 = "pqr"
print(max_attempts(ingredients2, target_meal2))

ingredients3 = "ingredientsforcooking"
target_meal3 = "cooking"
print(max_attempts(ingredients3, target_meal3))



# ================ Problem 2 ====================
def is_similar(sentence1, sentence2, similar_pairs):
    if len(sentence1) != len(sentence2):
        return False
    for pair in similar_pairs:
        if pair[0] not in sentence1 or pair[1] not in sentence2:
            return False
    return True

print("================ Problem 2 ====================")
sentence1 = ["my", "type", "on", "paper"]
sentence2 = ["my", "type", "in", "theory"]
similar_pairs = [ ["on", "in"], ["paper", "theory"]]

sentence3 = ["no", "tea", "no", "shade"]
sentence4 = ["no", "offense"]
similar_pairs2 = [["shade", "offense"]]

print(is_similar(sentence1, sentence2, similar_pairs))
print(is_similar(sentence3, sentence4, similar_pairs2))


# ================ Problem 3 ====================
def get_hint(secret, guess):
    bull, cow = 0, 0

    secret_lst = list(secret)

    for i in range (len(secret)):
        if secret[i] == guess[i]:
            bull += 1
            secret_lst.remove(guess[i])
        elif guess[i] in secret_lst:
            cow += 1
            secret_lst.remove(guess[i])
    
    return str(bull) + "A" + str(cow) + "B"


print("================ Problem 3 ====================")
secret1 = "1807"
guess1 = "7810"

secret2 = "1123"
guess2 =  "0111"

print(get_hint(secret1, guess1))
print(get_hint(secret2, guess2))


# ================ Problem 4 ====================
def count_winning_pairings(star_power):
    i, j = 0, 1
    count = 0
    while i < len(star_power) - 1:
        while j < len(star_power):
            num = star_power[i] + star_power[j]
            if num & (num - 1) == 0:
                count += 1
            j += 1
        i += 1
        j = i + 1
    return count

print("================ Problem 4 ====================")
star_power1 = [1, 3, 5, 7, 9]                       # check if the number is power of 2: n & (n - 1) == 0
print(count_winning_pairings(star_power1))

star_power2 = [1, 1, 1, 3, 3, 3, 7]
print(count_winning_pairings(star_power2))



# ================ Problem 5 ====================
def assign_unique_nicknames(nicknames):
    res = []
    count = 0
    for name in nicknames:
        if name in res:
            count += 1
            res.append(name + " (" + str(count) + ")")
        else:
            res.append(name)

    return res

print("================ Problem 5 ====================")
nicknames1 = ["Champ","Diva","Champ","Ace"]
print(assign_unique_nicknames(nicknames1))

nicknames2 = ["Ace","Ace","Ace","Maverick"]
print(assign_unique_nicknames(nicknames2)) 

nicknames3 = ["Star","Star","Star","Star","Star"]
print(assign_unique_nicknames(nicknames3))



# ================ Problem 6 ====================
def pair_contestants(scores, k):
    remainders = []
    for score in scores:
        remainders.append(score % k)

    total = sum(remainders)
    return total % k == 0


print("================ Problem 6 ====================")
scores1 = [1,2,3,4,5,10,6,7,8,9]      
k1 = 5
print(pair_contestants(scores1, k1))

scores2 = [1,2,3,4,5,6]
k2 = 7                                      
print(pair_contestants(scores2, k2))

scores3 = [1,2,3,4,5,6]
k3 = 10
print(pair_contestants(scores3, k3))