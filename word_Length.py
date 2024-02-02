# Build a function that uses a while loop to calculate the length of a
# string without using built-in functions.

user_Input = input('Enter a word or sentence: ');

def length(userInput):
    i = 0;
    count = 0;
    while userInput:
        userInput = userInput [1:]
        count += 1;
        i += 1;
    return count;

print(f'The length of {user_Input} : {length(user_Input)}');