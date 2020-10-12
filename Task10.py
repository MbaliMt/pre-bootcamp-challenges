
vowels = ['a','e','i','o','u']

def myString(word):
    for x in word:
        for n in vowels:
            if x == n:
                print(n, end=' ')

myString("This is a string".lower())
