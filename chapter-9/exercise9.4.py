addresses = dict()

fname = input('Enter a file name: ', )
fhand = open(fname, 'r')

for line in fhand:
    if line.startswith('From '):
        line = line.split()
        address = line[1]
        addresses[address] = addresses.get(address, 0)+1

max = 0
max_address = None
for key in addresses:
    if addresses[key] > max:
        max_address = key
        max = addresses[key]
    else:
        continue
print(max_address, max)
