

def word_count(s):
    
    split = s.split()

    word_dict = {}

    for s in split:
        s = s.lower()
        s = ''.join(filter(str.isalpha, s))
        # put words in a dictionary
        if s in word_dict:
            word_dict[s] += 1
        else:
            word_dict[s] = 1

    
    return word_dict




if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))