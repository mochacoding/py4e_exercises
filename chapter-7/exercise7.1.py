fname = input('Enter a file name: ', )
fhand = open(fname, 'r')
for line in fhand:
    line = line.rstrip()
    print(line.upper())