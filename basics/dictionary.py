captital = {
    "USA":"washinton BC",
    "India":"Delhi",
    "Maharastra":"Mumbai",
    "WB":"Kolkata"
}

# here the key:value are stored here we access the value with key

print(captital["WB"])

# print(captital["UP"]) error aara that 


# agar check karna hai toh 

print(captital.get("UP"))


print(captital.keys())

print(captital.values())

print(captital.items())


# using for loop

for key,value in captital.items():
    print(key,value)


## update used to update the key value already present in dictionary

captital.update({"WB":"Bangali"})



## update used to update the key value to add new value present in dictionary
captital.update({"UP":"Varanasi"})

print(captital) 

captital.pop("china")

captital.clear()
