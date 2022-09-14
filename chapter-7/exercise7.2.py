fname = input('Enter a file name: ', )
fhand = open(fname, 'r')
count = 0
total = 0

for line in fhand:
    if line.startswith('X-DSPAM-Confidence'):
        line = line.rsplit()
        line = line[1]
        count += 1
        total += float(line)
print('Average spam confidence: ', total/count)
        #print(line)