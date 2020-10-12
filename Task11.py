
def compareStrings(word1, word2):
    w1 = list(word1)
    w2 = list(word2)
    for char1 in word1:
        for char2 in word2:
            if char1 == char2:
                print(char1, end=" ")

compareStrings("mother".lower(), "mOon".lower())