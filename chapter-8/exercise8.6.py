total = 0
numbers = []

while True:
    num = input('Enter a number: ', )
    if num == 'done':
        break
    else:
        fnum = float(num)
        total += fnum
        numbers.append(fnum)

print(max(numbers))
print(min(numbers))