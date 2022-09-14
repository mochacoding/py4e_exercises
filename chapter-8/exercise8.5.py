fname = input('Enter a filename: ', )
fhand = open(fname, 'r')
count = 0

for line in fhand:
    if line.startswith('From '):
        line = line.split()
        sender = line[1]
        print(sender)
        count += 1 
print(f'There were {count} lines in the file with From as the first word')