# Build a function that reverse a given string

user_Input = input('Enter a string: ');
def reverse(text):
    reversedString = '';
    i = len(text) - 1;
    while i >= 0:
        reversedString += text[i];
        i -= 1;
    return reversedString;

print(f'{user_Input} in reverse = {reverse(user_Input)}');