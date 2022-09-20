# Exercise 2: This program counts the distribution of the hour of the day for each of the messages. You can pull the hour from the “From” line by finding the time string and then splitting that string into parts using the colon character. Once you have accumulated the counts for each hour, print out the counts, one per line, sorted by hour as shown below.

fname = input('Enter a file name: ', )
fhand = open(fname, 'r')

hours = {}

for line in fhand: 
    if line.startswith('From '):
        line = line.rsplit()
        time = line[5]
        time = time.split(':')
        hour = time[0]
        hours[hour] = hours.get(hour, 0 ) + 1

lhour = list(hours.items())
lhour.sort()
for key, value in lhour:
    print(key, value)