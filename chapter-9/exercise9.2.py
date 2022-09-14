words = dict()

fname = input('Enter a file name: ', )
fhand = open(fname, 'r')

for line in fhand:
    if line.startswith('From '):
        line = line.split()
        word = line[2]
        words[word] = words.get(word,0) + 1
print(words)
'''
        for word in line:
            word = line[2]
        words[word] = words.get(word, 0)+ 1
print(words)
'''