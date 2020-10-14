
def areaOfTriagle(a, b, c):
    semi = a + b + c
    semi = semi / 2

    areaT = float((semi * (semi - float(a)) * (semi - float(b)) * (semi - float(c))) ** 0.5)
    return areaT


print(areaOfTriagle(3, 4, 5))


