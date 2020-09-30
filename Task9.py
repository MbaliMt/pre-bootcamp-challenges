
count1 = 0
count2 = 0
for x in range(3, 1000, 3):
    print(x)
    count1 = count1 + x
for j in range(5, 1000, 5):
    print(j)
    if (x != j):
        count2 = count2 +j

print(count1 + count2)







