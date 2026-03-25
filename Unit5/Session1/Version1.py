# =============== Problem 1 ================= 
class Villager:
    def __init__(self, name, species, catchphrase):
        self.name = name
        self.species = species
        self.catchphrase = catchphrase
        self.furniture = []

print("=============== Problem 1 =================")
apollo = Villager("Apollo", "Eagle", "pah")
print(apollo.name)
print(apollo.species) 
print(apollo.catchphrase)
print(apollo.furniture)


# =============== Problem 2 =================
class Villager:
    def __init__(self, name, species, catchphrase):
        self.name = name
        self.species = species
        self.catchphrase = catchphrase
        self.furniture = []

    def add_item(self, item_name):
        validation = ["acoustic guitar", "ironwood kitchenette", "rattan armchair", "cacao tree"]

        if item_name in validation:
            self.furniture.append(item_name)

# time complexity - O(n)
# space complexity - O(n)
print("=============== Problem 2 =================")
alice = Villager("Alice", "Koala", "guvnor")
print(alice.furniture)

alice.add_item("acoustic guitar")
print(alice.furniture)

alice.add_item("cacao tree")
print(alice.furniture)

alice.add_item("nintendo switch")
print(alice.furniture)


# =============== Problem 3 =================
class Villager:
    def __init__(self, name, species, personality, catchphrase):
        self.name = name
        self.species = species
        self.personality = personality
        self.catchphrase = catchphrase
        self.furniture = []

def of_personality_type(townies, personality_type):
    res = []
    for person in townies:
        if person.personality == personality_type:
            res.append(person.name)
    return res
print("=============== Problem 3 =================")
isabelle = Villager("Isabelle", "Dog", "Normal", "what's up?")
bob = Villager("Bob", "Cat", "Lazy", "pthhhpth")
stitches = Villager("Stitches", "Cub", "Lazy", "stuffin'")

print(of_personality_type([isabelle, bob, stitches], "Lazy"))
print(of_personality_type([isabelle, bob, stitches], "Cranky"))



# =============== Problem 4 =================
class Villager:
    def __init__(self, name, species, personality, catchphrase, neighbor=None):
        self.name = name
        self.species = species
        self.personality = personality
        self.catchphrase = catchphrase
        self.furniture = []
        self.neighbor = neighbor

def message_received(start_villager, target_villager):
    while 
    # Nice brainstorm guys! Happy to work with you all

print("=============== Problem 4 =================")
isabelle = Villager("Isabelle", "Dog", "Normal", "what's up?")
tom_nook = Villager("Tom Nook", "Raccoon", "Cranky", "yes, yes")
kk_slider = Villager("K.K. Slider", "Dog", "Lazy", "dig it")
isabelle.neighbor = tom_nook
tom_nook.neighbor = kk_slider

# isabelle --> tom_nook --> kk_slider
print(message_received(isabelle, kk_slider))
print(message_received(kk_slider, isabelle))