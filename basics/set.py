utensil = {"knife", "cups", "cotton"}

for i in utensil:
    print(i)

utensil.add("spoon")

print(utensil)

# utensil.clear()

# print(utensil)

clothes = {"cotton", "wool", "silk"}

utensil.update(clothes)

clothes.update(utensil)

print(utensil)

uc= utensil.union(clothes)

print(uc)

# cu = 

#differce 

cu = utensil.difference(clothes)

print(cu)

commanelement = utensil.intersection(clothes)

print(commanelement)
