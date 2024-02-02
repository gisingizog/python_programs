#Write a Python program that will display the calculator menu.
# The program will prompt the user to choose the operation choice (from 1 to 5). Then it asks the user to input two integer values for 
#the calculation.  The function must be grouped in arithmetic namespace. See the sample below. 
# MENU 
#           1. Add 
#           2. Subtract 
#           3. Multiply 
#           4. Divide 
#           5. Modulus 
# Enter your choice: 1 
# Enter your two numbers: 12 15 
# Result: 27 
# Continue? y 
# The program also asks the user to decide whether he/she wants to continue the operation. If he/she input ‘y’, the program will prompt
# the user to choose the operation again. Otherwise, the program will terminate.

addition = lambda a,b : a + b;
subtraction = lambda a,b: a - b;
multiplication = lambda a,b: a * b;
division = lambda a,b: a / b;
modulus = lambda a,b: a % b;

def calculator():

    while True: 
        print('Calculator Application');
        print('MENU\n 1. Add\n 2. Subtract\n 3.Multiply\n 4.Divide\n 5.Modulus');

        choice = input('Enter your choice: ');
        inputs = input('Enter your two numbers: ').split(' ')
        firstNum, secondNum = inputs;

        if choice == '1':
            print('Result: ' +str(addition(int(firstNum),int(secondNum))));
        elif choice == '2':
            print('Result: ' +str(subtraction(int(firstNum),int(secondNum))));
        elif choice == '3':
            print('Result: ' +str(multiplication(int(firstNum),int(secondNum))));
        elif choice == '4':
            print('Result: ' +str(division(int(firstNum),int(secondNum))));
        elif choice == '5':
            print('Result: ' +str(modulus(int(firstNum),int(secondNum))));
        else: 
            print('Invalid Input')

        continue_Or_Not = input('Continue? (y/n) ');
        if continue_Or_Not.lower() != 'y':
            break;

calculator();