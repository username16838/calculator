print("I have a special calculator for calculating averages")
print("you can find it here | > https://github.com/username16838/calculator/blob/main/calc.py")

print('\n')

num = float(input('>>> '))
op = input('>>>')
num1 = float(input('>>> '))

# logic

while True:
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
    
    print("would you like to run again | y/n")

    run_again = input('>>> ')

    if run_again =='n':
        break
    else:
        continue
