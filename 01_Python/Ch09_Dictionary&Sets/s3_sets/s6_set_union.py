# Union: Combination of all unique elements.

# 3. set.union()

farm_animals = {"sheep", "hen", "cow", "horse", "goat"}
wild_animals = {"lion", "elephant", "tiger", "goat", "panther", "horse"}

all_animals_1 = farm_animals.union(wild_animals)
print(all_animals_1)

all_animals_2 = wild_animals.union(farm_animals)    # same result, returns a new set
print(all_animals_2)

all_animals_3 = wild_animals | farm_animals         # same result, returns a new set
print(all_animals_3)

wild_animals.update(farm_animals)           # updates the wild_animal with farm_animals and returns None
print(wild_animals)
