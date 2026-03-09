from collections import Counter
# ================ Problem 1 ====================
# M - use two pointer, dict
# P - use i, j; if abs(art_pieces[i] - art_pieces[j]) == 1
#   - add on the numbers of art_pieces[j] and numbers of art_pieces[i] in the art_pieces list
#   - store the number in an empty list
#   - return the max number and if the list is empty, return 0
def find_balanced_subsequence(art_pieces):
    freq = Counter(art_pieces)
    i, j = 0, 1
    all_substring = []
    while j < len(art_pieces):
        if abs(art_pieces[i] - art_pieces[j]) == 1:
            total_substring = freq[art_pieces[i]] + freq[art_pieces[j]]
            all_substring.append(total_substring)
        i += 1
        j += 1
    
    return max(all_substring) if all_substring else 0


print("================ Problem 1 ====================")
art_pieces1 = [1,3,2,2,5,2,3,7]
art_pieces2 = [1,2,3,4]
art_pieces3 = [1,1,1,1]

print(find_balanced_subsequence(art_pieces1))
print(find_balanced_subsequence(art_pieces2))
print(find_balanced_subsequence(art_pieces3))

# ================ Problem 2 ====================
# U - the max num of the art_pieces should == len(art_pieces) - 1
#   - besides of the max num, all num in the list need to be unique
# P - check if max num == len(list) - 1, else return False right away
#   - remove all max num in the list, and check are they unique
#   ** use while i < len(art_pieces) instead of i in range or for loop, after remove a number
#       it would not skip one index **
def is_authentic_collection(art_pieces):
    largest = max(art_pieces)
    if largest != len(art_pieces) - 1:
        return False
    verify = []
    i = 0
    while i < len(art_pieces):
        if art_pieces[i] == largest:
            art_pieces.remove(art_pieces[i])
        else:
            verify.append(art_pieces[i])
            i += 1
    return verify == art_pieces

print("================ Problem 2 ====================")
collection1 = [2, 1, 3]
collection2 = [1, 3, 3, 2]
collection3 = [1, 1]

print(is_authentic_collection(collection1))
print(is_authentic_collection(collection2))
print(is_authentic_collection(collection3))


# ================ Problem 3 ====================
# P - find the unique word in the list, then remove those word from the original list
#   - keep doing it until the original list len is 0
def organize_exhibition(collection):
    original = collection
    res = []
    while len(original) != 0:
        unique = set(collection)
        for word in unique:
            unique = list(unique)
            if word in original:
                original.remove(word)
            else:
                i += 1
        res.append(unique)
    return res


print("================ Problem 3 ====================")
collection1 = ["O'Keefe", "Kahlo", "Picasso", "O'Keefe", "Warhol", 
              "Kahlo", "O'Keefe"]
collection2 = ["Kusama", "Monet", "Ofili", "Banksy"]

print(organize_exhibition(collection1))
print(organize_exhibition(collection2))


# ================ Problem 4 ====================
# M - dict
# P - loop through each item in the list
#   - dict = {"modern.artmusuem.com": 9001, "artmusuem.com": 9001, "com": 9001]}
#   - dict = {"abstract.gallery.com": 900, "gallery.com": 900, "com": 900,
#             "impressionism.com": 50, "com": 50, .....}
#   - loop through each value and add "key" + value -> a string
def subdomain_visits(cpdomains):
    dict = {}

    for item in cpdomains:
        parts = item.split(" ")
        num = int(parts[0])
        url = parts[1]
        if url not in dict:
            dict[url] =  num
            while "." in url:
                dot_index = url.index(".")
                sub_url = url[dot_index+1:]
                dict[sub_url] = dict.get(sub_url, 0) + num
                url = sub_url
        else:
            dict[url] += num
    
    res = []
    for key, value in dict.items():
        temp_str = str(value) + " " + key
        res.append(temp_str)
        temp_str = ""

    return res

print("================ Problem 4 ====================")
cpdomains1 = ["9001 modern.artmuseum.com"]
cpdomains2 = ["900 abstract.gallery.com", "50 impressionism.com", 
              "1 contemporary.gallery.com", "5 medieval.org"]

print(subdomain_visits(cpdomains1))
print(subdomain_visits(cpdomains2))


# ================ Problem 5 ====================


print("================ Problem 5 ====================")
