fname = input('Enter a file name: ', )

try: 
    fhand = open(fname, 'r')
except:
    if fname == 'na na boo boo':
        print('NA NA BOO BOO TO YOU - You have been punk\'d!')
        quit()
    else:
        print('File cannot be opened: ',fname)
        quit()
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