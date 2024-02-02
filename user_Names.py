# Write a program in Python with a function which accepts the user's first
# and last name and print them in reverse order with a space between them
# Sample output
# Input First Name: Mugisha
# Input Last Name: Sam
# Name in reverse is: Sam Mugisha

firstName = input('First Name: ');
lastName = input('Last Name: ');

def reverse_name(a,b):
    temp = a;
    a = b;
    b = temp;
    return a+ ' ' +b;

reversed_Name = reverse_name(firstName,lastName);
print(f"Name in reverse: {reversed_Name}");