print('Welcome to the number counter!')

total = 0
count = 0
max = None
min = None

while True: 
    orig_num = input('Enter a number: ', )
    
    if orig_num == 'done':
        break
    else:
        try:
            num = int(orig_num)
        except:
            print('Invalid input')
            continue
        if count == 0:
            min = num
            max = num
        count += 1
        total += num
        if num > max: max = num
        if num < min: min = num
print(max, min)