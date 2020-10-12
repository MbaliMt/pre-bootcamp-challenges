
def menu():
    input1 = input("Select the below options\n[C] for celsius\n[F] for Fahrenheit\n")
    if(input1 == "C" or input1 == "c"):
            return celsiusToFara()
    if (input1 == "F" or input1 == "f"):
            return FaraToCelsius()


def celsiusToFara():
    celcsius = float(input("Enter celsius\n"))
    fara = float((celcsius * 9/5) + 32)
    return round(fara)


def FaraToCelsius():
    fara1 = float(input("Enter Fahrenheit\n"))
    celsius1 = float((fara1 -32) * 5/9)
    return round(celsius1)


print(menu())




