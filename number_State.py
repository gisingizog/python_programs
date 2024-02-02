# Write a program in C++ with a function to check whether a number is
# positive, negative or zero.

def check_number(a):
    if a > 0:
        return 'Greater than zero';
    elif a < 0:
        return 'Less than zero';
    else :
        return 'Equal to zero';

print(check_number(4));