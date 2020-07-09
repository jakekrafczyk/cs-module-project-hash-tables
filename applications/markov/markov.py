import random

'''
1. Read the file `input.txt` and split it into words.

   Don't worry about changing punctuation or capitalization. For
   example, a "word" might be `"Hello,`. Just leave it all in there.

2. Analyze the text, building up the dataset of which words can follow
   particular words.

   (Hint: leave duplicates in for this part. If a the word `and` is seen
   following the word `goats` multiple times, include all those `and`s.
   It'll give more convincing results because it is modelling the
   _frequency_ of _how often_ a word follows another word.)

3. Choose a random "start word" to begin.

4. Loop through:

   * Print the word.
   * If it's a "stop word", stop.
   * Else randomly choose a word that can follow this one.

Start words are words that begin with a capital, or a `"` followed by a
capital.

Stop words are words that end in any of the punctuation `.?!`, or that
punctuation followed by a `"`.

Hints:

* `random.choice()` can choose a random word out of a list.
* `print(s, end=" ")` will print a space after every word instead of a
  newline.
'''

# Read in all the words in one go
#with open("input.txt") as f:
f = open("applications/markov/input.txt",'r')
words = f.read()

words = words.split()
# TODO: analyze which words can follow other words
word_dict = {}
start_list= []
stop_list = []
for index,word in enumerate(words):
   #any(ele in test_string for ele in test_list) 
   if any(x in [".","?","!"] for x in word) or word[-1] == '"':
      stop_list.append(word)

   elif word[0].isupper() or word[0]== '"':
      start_list.append(word)
      if word in word_dict:
         if words[index+1] is not None:
            word_dict.setdefault(word, []).append(words[index+1])
      else:
         if words[index+1] is not None:
            word_dict[word] = [words[index+1]]

   else:
      if word in word_dict:
         if words[index+1] is not None:
            word_dict.setdefault(word, []).append(words[index+1])
      else:
         if words[index+1] is not None:
            word_dict[word] = [words[index+1]]

#print(word_dict)
#print(start_list)
# TODO: construct 5 random sentences
# Your code here

for x in range(5):
   word = random.choice(start_list)
   print(word,end=" ")
   
   while word:
      if word in stop_list:
         break
      else:
         word = random.choice(word_dict[word])
         print(word,end=" ")
