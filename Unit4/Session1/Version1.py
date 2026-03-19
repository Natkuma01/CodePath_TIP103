from collections import Counter
# ============ Problem 1 ===================
def filter_sustainable_brands(brands, criterion):
    res = []

    for item in brands:
        item["criteria_set"] = set(item["criteria"])
        
    for item in brands:
        if criterion in item["criteria_set"]:
            res.append(item["name"])
    return res

# time complexity - O(n * k)
# space complexity - O(n)

print("================ Problem 1 ====================")
brands = [
    {"name": "EcoWear", "criteria": ["eco-friendly", "ethical labor"]},
    {"name": "FastFashion", "criteria": ["cheap materials", "fast production"]},
    {"name": "GreenThreads", "criteria": ["eco-friendly", "carbon-neutral"]},
    {"name": "TrendyStyle", "criteria": ["trendy designs"]}
]

brands_2 = [
    {"name": "Earthly", "criteria": ["ethical labor", "fair wages"]},
    {"name": "FastStyle", "criteria": ["mass production"]},
    {"name": "NatureWear", "criteria": ["eco-friendly"]},
    {"name": "GreenFit", "criteria": ["recycled materials", "eco-friendly"]}
]

brands_3 = [
    {"name": "OrganicThreads", "criteria": ["organic cotton", "fair trade"]},
    {"name": "GreenLife", "criteria": ["recycled materials", "carbon-neutral"]},
    {"name": "FastCloth", "criteria": ["cheap production"]}
]

print(filter_sustainable_brands(brands, "eco-friendly"))
print(filter_sustainable_brands(brands_2, "ethical labor"))
print(filter_sustainable_brands(brands_3, "carbon-neutral"))



# ============ Problem 2 ===================
def count_material_usage(brands):
    count = {}
    for item in brands:
        for material in item["materials"]:
            if material not in count:
                count[material] = 1
            else: 
                count[material] += 1
    return count

# time complexity - O(n * m)
# space complexity - O(m)
print("================ Problem 2 ====================")
brands = [
    {"name": "EcoWear", "materials": ["organic cotton", "recycled polyester"]},
    {"name": "GreenThreads", "materials": ["organic cotton", "bamboo"]},
    {"name": "SustainableStyle", "materials": ["bamboo", "recycled polyester"]}
]

brands_2 = [
    {"name": "NatureWear", "materials": ["hemp", "linen"]},
    {"name": "Earthly", "materials": ["organic cotton", "hemp"]},
    {"name": "GreenFit", "materials": ["linen", "recycled wool"]}
]

brands_3 = [
    {"name": "OrganicThreads", "materials": ["organic cotton"]},
    {"name": "EcoFashion", "materials": ["recycled polyester", "hemp"]},
    {"name": "GreenLife", "materials": ["recycled polyester", "bamboo"]}
]

print(count_material_usage(brands))
print(count_material_usage(brands_2))
print(count_material_usage(brands_3))


# ================ Problem 3 ====================
def find_trending_materials(brands):
    materials = []
    res = []
    for item in brands:
        for material in item["materials"]:
            materials.append(material)

    freq = Counter(materials)

    for key, value in freq.items():
        if value > 1:
            res.append(key)

    return res
# time complexity - O(n * m)
# space complexity - O(n * m)
print("================ Problem 3 ====================")
brands = [
    {"name": "EcoWear", "materials": ["organic cotton", "recycled polyester"]},
    {"name": "GreenThreads", "materials": ["organic cotton", "bamboo"]},
    {"name": "SustainableStyle", "materials": ["bamboo", "recycled polyester"]}
]

brands_2 = [
    {"name": "NatureWear", "materials": ["hemp", "linen"]},
    {"name": "Earthly", "materials": ["organic cotton", "hemp"]},
    {"name": "GreenFit", "materials": ["linen", "recycled wool"]}
]

brands_3 = [
    {"name": "OrganicThreads", "materials": ["organic cotton"]},
    {"name": "EcoFashion", "materials": ["recycled polyester", "hemp"]},
    {"name": "GreenLife", "materials": ["recycled polyester", "bamboo"]}
]

print(find_trending_materials(brands))
print(find_trending_materials(brands_2))
print(find_trending_materials(brands_3))




# ================ Problem 4 ====================
def find_best_fabric_pair(fabrics, budget):
    fabric_dict = dict(fabrics)
    res = []

    fabric_dict = sorted(fabric_dict.items(), key=lambda item: item[1])

    i, j = 0, len(fabric_dict)-1
    while i < j:
        if fabric_dict[i][1] + fabric_dict[j][1] > budget:
            j -= 1
        elif fabric_dict[i][1] + fabric_dict[j][1] == budget:
            res.append(fabric_dict[i][0])
            res.append(fabric_dict[j][0])
            break
        else:
            i += 1

    return res
# time complexity - O(n log n)
# space complexity - O (n)
print("================ Problem 4 ====================")
fabrics = [("Organic Cotton", 30), ("Recycled Polyester", 20), ("Bamboo", 25), ("Hemp", 15)]
fabrics_2 = [("Linen", 50), ("Recycled Wool", 40), ("Tencel", 30), ("Organic Cotton", 60)]
fabrics_3 = [("Linen", 40), ("Hemp", 35), ("Recycled Polyester", 25), ("Bamboo", 20)]

print(find_best_fabric_pair(fabrics, 45))
print(find_best_fabric_pair(fabrics_2, 70))
print(find_best_fabric_pair(fabrics_3, 60))



# ================ Problem 5 ====================
def organize_fabrics(fabrics):
    sorted_fabric = sorted(fabrics, key=lambda item: item[1], reverse=True)
    res = []

    for item in sorted_fabric:
        res.append(item[0])
    return res
# time complexity - O(n log n)
# space complexity = O(n)
print("================ Problem 5 ====================")
fabrics = [("Organic Cotton", 8), ("Recycled Polyester", 6), ("Bamboo", 7), ("Hemp", 9)]
fabrics_2 = [("Linen", 5), ("Recycled Wool", 9), ("Tencel", 7), ("Organic Cotton", 6)]
fabrics_3 = [("Linen", 4), ("Hemp", 8), ("Recycled Polyester", 5), ("Bamboo", 7)]

print(organize_fabrics(fabrics))
print(organize_fabrics(fabrics_2))
print(organize_fabrics(fabrics_3))



# ================ Problem 6 ====================
def process_supplies(supplies):
    sorted_supplies = sorted(supplies, key=lambda item: item[1], reverse=True)
    res = []

    for item in sorted_supplies:
        res.append(item[0])
    
    return res
# time complexity - O(n log n)
# space complexity = O(n)

print("================ Problem 6 ====================")
supplies = [("Organic Cotton", 3), ("Recycled Polyester", 2), ("Bamboo", 4), ("Hemp", 1)]
supplies_2 = [("Linen", 2), ("Recycled Wool", 5), ("Tencel", 3), ("Organic Cotton", 4)]
supplies_3 = [("Linen", 3), ("Hemp", 2), ("Recycled Polyester", 5), ("Bamboo", 1)]

print(process_supplies(supplies))
print(process_supplies(supplies_2))
print(process_supplies(supplies_3))



# ================ Problem 7 ====================
def calculate_fabric_waste(items, fabric_rolls):
    return sum(fabric_rolls[i] - items[i][1] for i in range (len(items)))

# time complexity - O(n)
# space complexity - O(1)
print("================ Problem 7 ====================")
items_1 = [("T-Shirt", 2), ("Pants", 3), ("Jacket", 5)]
fabric_rolls_1 = [5, 5, 5]

items_2 = [("Dress", 4), ("Skirt", 3), ("Blouse", 2)]
fabric_rolls_2 = [4, 4, 4]

items_3 = [("Jacket", 6), ("Shirt", 2), ("Shorts", 3)]
fabric_rolls_3 = [7, 5, 5]

print(calculate_fabric_waste(items_1, fabric_rolls_1))
print(calculate_fabric_waste(items_2, fabric_rolls_2))
print(calculate_fabric_waste(items_3, fabric_rolls_3))



# ================ Problem 8 ====================
def organize_fabric_rolls(fabric_rolls):
    sorted_rolls = sorted(fabric_rolls)
    res = []
    for i in range (0, len(sorted_rolls)-1, 2):
            res.append((sorted_rolls[i], sorted_rolls[i+1]))

    if len(fabric_rolls) % 2 != 0:
        res.append(sorted_rolls[-1])

    return res

# time complexity - O(n log n)
# space complexity - O(n)
print("================ Problem 8 ====================")
fabric_rolls = [15, 10, 25, 30, 22]
fabric_rolls_2 = [5, 8, 10, 7, 12, 14]
fabric_rolls_3 = [40, 10, 25, 15, 30]

print(organize_fabric_rolls(fabric_rolls))
print(organize_fabric_rolls(fabric_rolls_2))
print(organize_fabric_rolls(fabric_rolls_3))