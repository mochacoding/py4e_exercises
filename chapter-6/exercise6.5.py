str = 'X-DSPAM-Confidence:0.8475'

new = str.find(':')

fnew = float((str[new+1:]))
print(fnew)



