# ================ Problem 1 ====================
def map_chambers(sections):
    if not sections:
        return 0
    if len(sections) == 1:
        return 1
    return 1 + map_chambers(sections[1])

print("================ Problem 1 ====================")
sections = ["Atlantis", ["Coral Cave", ["Pearl Chamber"]]]
print(map_chambers(sections))



# ================ Problem 2 ====================
def longest_trident_sequence(gems):
    pass

print("================ Problem 2 ====================")
print(longest_trident_sequence([1, 2, 3, 2, 3, 4, 5, 6]))
print(longest_trident_sequence([5, 10, 7, 8, 1, 2]))