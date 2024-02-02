# Write a function that converts the entered string to Uppercase

inputText = input('Enter a text: ');

def toUpperCase(value):
    return value.upper();

print(f'{inputText} in uppercase: {toUpperCase(inputText)}');