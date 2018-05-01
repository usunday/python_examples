def checkio(words):
    words = words.split()

    count = 0
    for w in words:
        if w.isalpha():
            count += 1
        else:
            count = 0

        if count == 3:
            return True

    return False

print(checkio("bla bla bla bla"))