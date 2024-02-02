#Write a program in Python to swap two numbers.
first = input("Number 1: ");
second = input("Number 2: ");
print("Before swapping \n Number 1: " + str(first) + " \n Number 2: " + str(second));

temp = first;
first = second;
second = temp;
print("After swapping \n Number 1: " + str(first) + " \n Number 2: " + str(second));
