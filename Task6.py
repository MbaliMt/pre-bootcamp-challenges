myList = []
def findMax(num1, num2, num3):
    myList.append(num1)
    myList.append(num2)
    myList.append(num3)
    for i in range(0, len(myList), 1):
        for j in range(i, len(myList), 1):
            if (myList[i] > myList[j]):
                temp = myList[i]
                myList[i] = myList[j]
                myList[j] = temp
    return myList[-1]
print("The maximum number is:", findMax(72,90, 1))


