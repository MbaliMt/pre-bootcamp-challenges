
def twoNumbers(num1, num2):
    sum = num1 + num2
    print(sum)
    if num1 == 3 or num2 == 3 and 3 in sum:
        return True
    else:
        return False


print(twoNumbers(10,3))