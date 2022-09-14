fname = input('Enter a file name: ', )
fhand = open(fname, 'r')

domains = dict()

for line in fhand:
    if line.startswith('From '):
        line = line.split()[1]
        # Because python is top down and left > right you can get the right slice by just putting the [1] afterwards. Saves a couple lines of code. 
        # line = line[1]
        key = line.split('@')[1]
        # key = line[1]
        domains[key] = domains.get(key, 0) + 1
print(domains)
