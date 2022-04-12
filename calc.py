# ui

num = float(input('>>> '))
op = input('>>>')
num1 = float(input('>>> '))

# logic

if op =='+':
    sum = num + num1
    print('>>> ' + str(sum))
if op =='-':
    sum = num - num1
    print('>>> ' + str(sum))
if op =='*':
    sum = num * num1
    print('>>> ' + str(sum))
if op =='/':
    sum = num / num1
    print('>>> ' + str(sum))