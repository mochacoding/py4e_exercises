try:

    hours = float(input('Enter Hours: ', ))
    rate = float(input('Enter Rate: ', ))

except:
    print('Error, please enter numeric input')
    quit()

if hours < 40:
    print('Pay: ', hours*rate)

if hours > 40:
    hot = hours-40
    rot = (.5*(rate))
    print('Pay: ', (hours*rate)+(hot*rot))
    