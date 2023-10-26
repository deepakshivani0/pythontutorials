name = "Muskan"

# to get the length of string
print(len(name))

print(name[5])

print(name[-1])

print(name[len(name)-1])


"""
M -> 0 -6
u -> 1 -5
s -> 2 -4
k -> 3 -3
a -> 4 -2
n -> 5 -1
 
"""

# use this slcing if u want to extract multiple characters
# end position will be excluded

# variable[startPos:endPos] 

print(name[0:4])

print(name[:4])

print(name[0:])

print(name[0:5154545])


# variable[startPos:endPos:jumpCount] 
str="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
print(str[12:15:3]) #it will jump 2 characters and give u every 3rd character

print(str.lower())

print(name.replace("Mus", "Dee"))


