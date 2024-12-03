# 2-D lists
pName = ["Tanmay", "Samiksha"]  # This list becomes the 0th index in the 2-D family
child = ["sam", "tan"]  # This list becomes the 1st index in the 2-D family

family = [pName, child]  # Here, family[0][0] will print "Tanmay"

# Nested loop to print all elements
for i in family:  # i iterates over the sublists in family
    for j in i:   # j iterates over the elements in each sublist
        print(j)

# another method for printing explicitly

for i in range(len(family)):  # Loop through the indices of the outer list
    for j in range(len(family[i])):  # Loop through the indices of each sublist
        print(family[i][j])

