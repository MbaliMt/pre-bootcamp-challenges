from collections import OrderedDict

list1 = []
list2 = []

sum = 0
for x in range(3, 1000, 3):
    list1.append(x)

for j in range(5, 1000, 5):
    list2.append(j)

list1.extend(list2)
nonDuplicateList = list(OrderedDict.fromkeys(list1))
list1.sort()
for z in nonDuplicateList:
    sum += z

# print(nonDuplicateList)
print("The sum of all the multiples of 3 or 5 below 1000 is:", sum)






