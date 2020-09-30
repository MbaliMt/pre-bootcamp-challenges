
vowels = ['a','e','i','o','u']

def myString(word):
    for x in vowels:
        for n in word:
            if x == n:
                print(x, end=' ')

myString("This is a string".lower())
