# ask for input
# def options (1,2,3,4)
# oprations 
# print

import sys

def add(a, b):
    answer = a + b
    print(str(a)+ "+" + str(b)+ "=" +str(answer))
    

def sub(a, b):
    answer = a - b
    print(str(a)+ "-" + str(b)+ "=" + str(answer))

def mult(a, b):
    answer = a * b
    print(str(a) + "*" + str(b)+ "=" + str(answer))

def div(a, b):
    if b == 0:
        print("Division by 0 is invalid")
        menu()

    answer = a / b
    print(str(a) + "/" + str(b) + "=" + str(answer))

def menu():
    print('Choose an operation: ')
    print('1. Addition')
    print('2. Subtraction')
    print('3. Multiplication')
    print('4. Division')
    print('5. EXIT')

    
    option = int(input('Enter your option: '))
    
    if option == 5:
        sys.exit()
    
    try:
        a = float(input("Ist Number: "))
        b = float(input("2nd Number: "))
    except ValueError or EOFError:
        print('Invalid Operation')
        menu()

    if option == 1:
        add(a, b)
    elif option == 2:
        sub(a, b)
    elif option == 3:
        mult(a, b)
    elif option == 4:
        div(a, b)
    else:
        print("Invalid Option ")
        menu()   

def main():
    menu()
    sys.exit()

if __name__ == '__main__':
    main()