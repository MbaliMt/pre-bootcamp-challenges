#
# count1 = 0
# count2 = 0
# list1 = []
# for x in range(3, 1000, 3):
#     print(x)
#     count1 = count1 + x
# for j in range(5, 1000, 5):
#     print(j)
#     # if (x == j):
#     count2 = count2 +j
#
# print(count1 + count2)

list1 = []
list2 = []
for x in range(3, 1000, 3):
    list1.append(x)
    print(list1)
for j in range(5, 1000, 5):
    list2.append(j)
    print(list2)
for m in list2:
    if m in list1:
        list2.remove(m)

        print(m)






