# Exercise 1: Revise a previous program as follows: Read and parse the “From” lines and pull out the addresses from the line. Count the num- ber of messages from each person using a dictionary.
# After all the data has been read, print the person with the most commits by creating a list of (count, email) tuples from the dictionary. Then sort the list in reverse order and print out the person who has the most commits.
# Sample Line:
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# Enter a file name: mbox-short.txt
# cwen@iupui.edu 5
# Enter a file name: mbox.txt
# zqian@umich.edu 195

fname = input('Enter a file name: ', )
fhand = open(fname, 'r')

addresses = {}
for line in fhand: 
    if line.startswith('From '):
        line = line.rsplit()
        address = line[1]
        addresses[address] = addresses.get(address, 0 ) + 1

ladd = []

new_list = list(addresses.items())
for email, count in list(addresses.items()):
    ladd.append((count, email))
ladd.sort(reverse=True)
first = list(ladd[0])
print(first[1], first [0])
