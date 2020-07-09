# Use frequency analysis to find the key to ciphertext.txt, and then
# decode it.

f = open("applications/crack_caesar/ciphertext.txt",'r')
words = f.read()

'''
Write a program that automatically finds the key for the ciphertext in
the file [`ciphertext.txt`](ciphertext.txt), then decodes it and shows
the plaintext.

(All non-letters should pass through the decoding as-is, i.e. spaces and
punctuation should be preserved. The input will not contain any
lowercase letters.)
'''

# need to split the words into characters, count them with a dictionary, sort them by frequency, and
# then replace each letter with the new letter

# or, could just iterate throughout the whole list and ignore space/punctuation
#words = words.split()
word_dict = {}

for x in words:
    if x.isalpha():
        if x in word_dict:
            word_dict[x] += 1
        else:
            word_dict[x] = 1

#now sort
word_items = list(word_dict.items())

word_items.sort(key=lambda x: x[1],reverse=True)

# now swap each 
keylist = ['W','J','M','X','C','D','K','I','N','U','S','O','G','Q','B','Y','E','F','A','Z','P','H','V','T','L','R']
vlist = ['E', 'T', 'A', 'O', 'H', 'N', 'R', 'I', 'S', 'D', 'L', 'W', 'U',
'G', 'F', 'B', 'M', 'Y', 'C', 'P', 'K', 'V', 'Q', 'J', 'X', 'Z']
swap_dict = dict(zip(keylist,vlist))


en_words = list(enumerate(words))

for index, x in en_words:
    if x.isalpha():
        new = swap_dict[x]
        x = new
    
    print(x,end="")

