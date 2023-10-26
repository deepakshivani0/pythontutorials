# for i in range(5):
#     print(i)

# range(startPos, endPos, jump)   endPos will be excluded
str1="ajksdfhbjk"


print(str1[2:8:2])

for i in range(10, 17, 2):
    print(i)

# List can contain any datatypes inside it
lst1=[1,2,3,"hello", 1.02, True]

lst2=[1,2,3,4,5,6,4]



# slicing of list
print(lst1[1:5:2])

# functions of list
print(len(lst1))
lst1.append(2546)
lst1.extend(lst2)
lst1.insert(1, "muskan")
print(lst1.index("muskan"))
lst1.remove("hello")
print(lst1)

#  Tuple is immutable and cant be updated once created
# Tuples and its functions
tup1=(1,2,3,4,5,3,4,3,1,12,3)
print(tup1.index(3))

lst1.append(lst2)
print(lst1)

# Dictionary is key-value pair
# key is always immutable and is used to access the value
# value can be anything

myGF= {"name":"Muski", "height":5.4, "shoeNumber":7, "herFriend":["Amit", "Tanisha", "Abhinav"], "angerIssue":True}

# accessing elements to dict
print(myGF["name"])
print(myGF["herFriend"])

# Add new elements to dict
myGF["herBF"]="BUBU"

print(myGF)

# functions of dict

# print(myGF["from"])
print(myGF.get("from", "Bihar"))
print(myGF.keys())
# myGF.get()

# Set is similiar as list, only difference is that set will not allow duplicate data. and it will not have index based access

mySet={1,2,3,4,5,6,1}
print(mySet)
# print(mySet[0]) this will cause u error, as indexing is not allowed in sets

mySet.add("2")
print(mySet)

