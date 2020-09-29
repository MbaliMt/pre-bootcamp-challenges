
def maxNumber(num1, num2, num3):
    numlist = []
    numlist.append(num1)
    numlist.append(num2)
    numlist.append(num3)

    for x in range(0, 3):
        for m in range(x, 3):
            if (numlist[x] > numlist[m]):
                temp = numlist[x]
                numlist[x] = numlist[m]
                numlist[m] = temp
                for z in numlist:
                    print(numlist[-1])
            
maxNumber(100, 60, 45)



