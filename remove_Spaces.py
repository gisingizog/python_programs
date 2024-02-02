# Write a function that removes all spaces in a string and print the
# resulting string.

inputValue = input('Enter a text with spaces: ');

def remove_Space(text):
    return text.replace(' ','');

print(f'{inputValue} without space : {remove_Space(inputValue)}');