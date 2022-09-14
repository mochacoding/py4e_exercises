words = []

fname = input('Enter a filename: ', )
fhand = open(fname, "r")

for line in fhand:
    line = line.split()
    for word in line:
        if word not in words:
            words.append(word)
            words.sort()

print(words)