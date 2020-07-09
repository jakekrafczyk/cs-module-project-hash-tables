'''
Print a histogram showing the word count for each word, one hash mark
for every occurrence of the word.

Output will be first ordered by the number of words, then by the word
(alphabetically).

The hash marks should be left justified two spaces after the longest
word.
print(f'{word}  {#*count})

Case should be ignored, and all output forced to lowercase.

Split the strings into words on any whitespace.

Ignore each of the following characters:

```
" : ; , . - + = / \ | [ ] { } ( ) * ^ &
```

If the input contains no ignored characters, print nothing.

## Hints

Items: `.items()` method on a dictionary might be useful.

Sorting: it's possible for `.sort()` to sort on multiple keys at once.

Sorting: negatives might help where `reverse` won't.

Printing: you can print a variable field width in an f-string with
nested braces, like so `{x:{y}}`
'''

# REGEX, SPLIT AND LOWER
# first need to import the text and split it into a list of words
text = open('applications/histo/robin.txt','r')
read = text.read().split()

word_dict = {}

for s in read:
    s = s.lower()
    s = ''.join(filter(str.isalpha, s))
    # put words in a dictionary
    if s in word_dict:
        word_dict[s] += 1
    else:
        word_dict[s] = 1


# now we need to sort and print it
dict_items = word_dict.items()
#print(dict_items)
dict_items = sorted(dict_items)
#print(dict_items)
dict_items = sorted(dict_items,key = lambda x: x[1],reverse=True)

# now print with hash marks
for x in dict_items:
    print(f'{x[0]}  {x[1]}')