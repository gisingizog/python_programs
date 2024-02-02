# Build a function that check if an entered character is a digit or alpha
# letter.

user_Input = input('Enter any character: ');

def isDigit(userInput):
    numbers = ['0','1','2','3','4','5','6','7','8','9'];
    if userInput in numbers :
        return True;
    else:
        return False;

if(isDigit(user_Input)):
    print(f'{user_Input} is digit');
else :
    print(f'{user_Input} is an alpha character');
