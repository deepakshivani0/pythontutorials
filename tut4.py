
# 1st question

# ["1", "2", "3", "4", "5", "6"] - Input List

# 1.1["odd", "even", "odd", "even", "odd", "even"] - #Expected List

# 1.2{1:"odd", 2:"even", 3:"odd", 4:"even", 5:"odd", 6:"even"} #- #Expected Dict

lst1= ["1", "2", "3", "4", "5", "6"] 
result=[]
for i in lst1:
    if int(i)%2==0:
        result.append("even")
    else:
        result.append("odd")

print(result)

resultDict={}
for i in lst1:
    if int(i)%2==0:
        resultDict[i]="even"
    else:
        resultDict[i]="odd"

print(resultDict)

# 2nd question

# list1 = ['apple', 'orange', 'mango', 'pineapple', 'papaya', 'avacado', 'strawberry', 'pear']

# list2 = ['orange', 'apple', 'pineapple', 'mango', 'avacado', 'papaya', 'pear','strawberry']

list1 = ['apple', 'orange', 'mango', 'pineapple', 'papaya', 'avacado', 'strawberry', 'pear']

# 1 way of doing it. by storing the swapped elements in new list
resultList=[]
for i in range(0, len(list1), 2):
    resultList.append(list1[i+1])
    resultList.append(list1[i])
print(resultList)

# for reference
tmp=[1,2,3,4,5,6]

for i in range(0,len(tmp), 2):
    print(tmp[i])
    print(tmp[i+1])

for i in range(0,len(tmp), 2):
    print(tmp[i+1])
    print(tmp[i])

# 2nd way of doing it by updating the list 

tmp=0
for i in range(0, len(list1), 2):
    tmp=list1[i]
    list1[i]=list1[i+1]
    list1[i+1]=tmp

print(list1)

# If else conditions

name = input("Please enter your name")

if(name.lower()=="antra"):
    print(f"Hello {name}")
    print("Ran if antra")


if(name.lower()=="deepak"):
    print(f"Hello {name}")
    print("Ran if deepak")
elif(name.lower()=="deepak"):
    print(f"Hello {name}")
    print("Ran elif deepak")
else:
    print(f"Hello Unknown")

# f string

myGf= "Antra"

print("The World cutiest girl is "+myGf)
print(f"The World's cutiest girl is {myGf}")

    




