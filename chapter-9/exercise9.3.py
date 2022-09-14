addresses = dict()

fname = input('Enter a file name: ', )
fhand = open(fname, 'r')

for line in fhand:
    if line.startswith('From '):
        line = line.split()
        address = line[1]
        addresses[address] = addresses.get(address, 0)+1
print(addresses)
    