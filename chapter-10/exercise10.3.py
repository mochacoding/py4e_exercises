# Exercise 3: Write a program that reads a file and prints the letters in decreasing order of frequency. Your program should convert all the input to lower case and only count the letters a-z. Your program should not count spaces, digits, punctuation, or anything other than the letters a-z. Find text samples from several different languages and see how letter frequency varies between languages. Compare your results with the tables at https://wikipedia.org/wiki/Letter_frequencies.

import string
fname = input('Enter a file name: ')
fhand = open(fname, 'r') 
# text = fhand.read()
wdict = {}
ldict = []
"""
for l in text:
    # print(l)
    l = l.translate(l.maketrans("","",string.punctuation))
    l = l.translate(l.maketrans("","",string.digits))
    l = l.translate(l.maketrans('','',string.whitespace))
    l = l.lower()
    for letter in l:
        wdict[letter] = wdict.get(letter, 0) + 1 
for ch, count in list(wdict.items()):
    ldict.append((ch, count))
ldict.sort()
print(ldict)
"""
# print(l)

for line in fhand:
    line = line.rstrip()
    nline = line.lower()
    nline = nline.translate(nline.maketrans("","",string.punctuation))
    nline = nline.translate(nline.maketrans('','',string.digits))
    words = nline.split()
    for word in words:
        letter = list(word)
        for l in letter: 
            wdict[l] = wdict.get(l, 0) + 1
letters = list(wdict.items())
for key, value in letters:
    ldict.append((value, key))
ldict.sort(reverse=True)
print(ldict)
#     for word in words:
#         wdict[word] = wdict.get(word, 0) + 1
# print(wdict)
    # print(words)

    # print(nline)
