name = "Tanmay"
# age = 69
# # print("Hello tanmay") 
# # print(name)
# # print(age*5)
# # age = age/69 
# # print(age)   
print("Heyy "+name)
# # lastname= " Gupta"
# # fulname = name + lastname 
# # print(fulname)
# age += 59
# print(age)

# ## type will tell the data type of our variable

# a = 65 
# print(type(a))
# print(type(age))
# print(type(name))
# print("The age is : "+ str(age)) ## typecasting we were not able to display age
# ##(int) with string (The age is : ) so we do type casting here
# print(type(age))    

# ## type casting str() used for variable of differnt datatype to convert in string


# ## floating point number 
# height = 255.096
# print(height)
# print(type(height))
# # print("My height is : "+height) gives an error so we need to convert float height to string height 
# print("My height is : "+str(height)) ## typecasting we were not able to display height


# ## boolean value 
# humans = True 
# woman = False 
# print(humans)
# print(woman)

# ## datatype of human   
# print(type(humans))
# print(type(woman))
# print("the human are :"+str(humans))

# # Multiple assignment = allow us to assign multiple variable in same line of code 

# name , age , sex = "Tanmay" , 20 , "Male"

# # if value of multiple variable is same then

# n = a = b = 100

# print(n)
# print(a)
# print(b)

## string methods 


# xname = "Aayush Gupta"

# print(len(xname)) #lenght of string is no. if letter in string 
# print(xname.capitalize())
# print(xname.find("h")) # ye index dega milne ke baad 
# print(xname.upper()) # uppercase kar deta hai 
# print(xname.lower()) # lowercase kar deta hai
# print(xname.isdigit()) # if tere is a number in string the return true/false 
# # print(xname.isalpha) 
# print(xname.count("a"))
# print(xname.replace("a","t"))
# print(xname*3)


# type casting is converting the data type of a value to anaother data type

# a,b,c = 1,2.0,"3" # here a is int & b is float & c is string 
# print(type(a))
# print(type(b))
# print(type(c))

# # to convert all to an int() using type casting  
# x = int(a)
# y = int(b)
# z = int(c)

# print(x)
# print(y)
# print(z)


# # to convert all to an float() using type casting 
# x = float(a)
# y = float(b)
# z = float(c)

# print(x)
# print(y)
# print(z)


# # to convert all to an str() using type casting 
# x = str(a)
# y = str(b)
# z = str(c)

# print(x)
# print(y)
# print(z)

# ## input from user in python 
# name = input("what is your name? ")
# print("Hello "+name)

# ## all input from user are taken as string but if we want to add int from user input is not possible 
# ## we have to perform typw casting 

# age = int(input("How old are you? "))
# # age = age + 1 
# # print("your age is : "+age) so for this we need to type cast age
# # age = int(age) + 1
# print("your age is : "+str(age)) # here we have to typecast age to string to print our age(whch is int) with string

# height = float(input("how tall are you ?"))
# print("i am "+str(height)+" cm tall") # here we have to typecast height to string


## maths method 

# import math 

# pi = 3.14 
# x,y,z = 1,2,3

# print(round(pi)) ## roundup the value to nearest integer 
# print(math.ceil(pi)) ## roundup to next interger
# print(math.floor(pi)) ## roundup to previous integer 
# print(abs(pi)) ## abs() is absolute value of if pi = -3.14 then absolute value is 3.14 means zero se kitna duur hai 
# print(pow(pi,3)) ## pow() is used to raise the power of variable 
# print(math.sqrt(121)) ## this math.sqrt() is used to find the root of any number 
# print(max(x,y,z)) ## max() is used to find the maximum value 
# print(min(x,y,z)) ## min() is used to find the minimum value


## slicing : creating a sub string by extracting it from another string 
## called indexing[] or slice() where there are 3 argument [start:stop :step]

## for [start:stop]
# name = "Aayush Gupta"
# name1 = "Tanmay Gupta"


# firstName = name[0:6] ## to print subString as aayush we have to index as :
#                     ## the 0 in the limit is inclusive and 6 in the limit is exclusive 

# lastName = name[7:12]
# print(firstName)
# print(lastName)

# ## for [start:stop:step]

# # funckyName = name[0:12:2]
# funckyName = name[:6:2] ## all represntation is same 
# # funckyName = name[::2]
# print(funckyName)

## reverse name or reversing string using slicing or indexing 

# reverseName = name[::-1]
# print(reverseName)

# reverseName1 = name1[::-1]
# print(reverseName1)

##  slice ka use :

# website1 = "http://flipkart.com"
# website2 = "http://wikipedia.com"
# slice = slice(7,-4)

# print(website1[slice])
# print(website2[slice])

## logical operator && , || , != (and , or , not)

## temp wala eg

# temp = int(input("What is the temperature outside"))

# if temp>=0 and temp<=30:
#     print("Temperature is good today")
#     print("You can go out")

# elif temp<=0 or temp<=30:
#     print("Temperature is not good today")
#     print("You can't go out")


# ## not logical operator 
# if not(temp>=0 and temp<=30):
#     print("Temperature is good today")
#     print("You can go out")

# elif (temp<=0 or temp<=30):
#     print("Temperature is not good today")
#     print("You can't go out")

## while loop : the statement or a block of code that will be executed until the condition remain true 

# while 1 == 1:
#     print("Fuck off")

# name = ""

# while len(name) == 0:
#     name = input("Enter your name : ")

# print("hello"+name)

## for loop : a statement that will execute a block of code a limmited ammount of time
        ## while loop is unlimited 
        ## for loop is limited 

# for i in range(10) :
#     print(i)     ## where the range is 0(inclusive) to 10 and 10 in exclusive 


# for i in range(100,200):
#     print(i)     ## where the range is 100(inclusive) and 200 in exclusive

## count up by 2 
for i in range(50,100+1,2):
    print(i) 

## how to print each letter in a string 
for i in "Tanmay":
    print(i)
