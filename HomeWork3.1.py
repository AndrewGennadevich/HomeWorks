#калькулятор
contin = 'k'
while contin == 'k':
    num1 = float(input("Enter u first number"))
    operation = input("enter u operation")
    num2 = float(input("enter u second number"))
    if operation == '+':
        print('Summ of numbers is:' + str(float(num1 + num2)))
    elif operation == '-':
        print('subtraction of numbers is:' + str(float(num1 - num2)))
    elif operation == '*':
        print('calculation is:' + str(float(num1 * num2)))
    elif operation == '/':
        print('calculation is:' + str(float(num1 / num2)))
    else:
        print("Error")
    contin = input("Enter 'k' if u want to be contin this process or other later if u want to stop this shit")



