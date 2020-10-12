
def twoNumbers(num1, num2):
    sum = num1 + num2
    sumToList = list(map(int, str(sum)))
    print(sumToList)
    print(sum)
    if num1 == 3 or num2 == 3 or 3 in sumToList:
        return True
    else:
        return False

print(twoNumbers(126, 4))

