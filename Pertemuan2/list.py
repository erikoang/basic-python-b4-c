#Penambahan dan pembuatan List
myList = [4, 5.3, "apple"]
#         0   1      2
myList.append(1)
myList.append(2)
myList.append(3)

#Cara output
print(myList)
print(myList[3])
print(myList[0:4])

#Output List satu persatu pake perulangan
for x in myList:
    print(x)