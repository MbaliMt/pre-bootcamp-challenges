import math

def numberToTime(number):
    timeInHours = number/60
    realTimeInNumbers = math.trunc(timeInHours)
    timeInMinutes = realTimeInNumbers * 60
    realTimeInMinutes = number - timeInMinutes
    print("The time is {} HOURS {} MINUTES".format(realTimeInNumbers, realTimeInMinutes))

print(numberToTime(266))