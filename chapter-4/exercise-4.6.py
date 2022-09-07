def computepay(hours,rate):

    try: 
        fhours = float(hours)
        frate = float(rate)
    except: 
        print('Enter numerical input')
        quit()
    if fhours < 40:
        pay = fhours * frate
        print('Pay: ', pay)
    if fhours > 40:
        hot = (fhours - 40)
        rot = (.5 * frate)
        pay = (fhours*frate) + (hot*rot)
        print('Pay: ', pay)

computepay(hours = input('Enter Hours: '), rate = input('Enter Rate: '))