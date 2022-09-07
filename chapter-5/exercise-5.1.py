print('Welcome to the number counter!')

total = 0
count = 0

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
        count += 1
        total += num
print(total,count, (total/count))