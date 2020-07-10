def no_dups(s):
    # get rid of duplicates with 0(n) runtime
    lookup = []
    words = s.split(" ")
    for index, word in enumerate(words):
        if word not in lookup:
            lookup.append(word)
        else:
            words.pop(index)
    print(words)
    return words



if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))