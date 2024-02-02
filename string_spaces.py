# Build a function that checks the number of spaces in a given string.

sentence = input('Input string: ');

def spaceCount(text):
    i = 0;
    count = 0;
    while i < len(text):
        if text[i] == ' ':
            count += 1;
            i += 1;
        else:
            i += 1;

    return count;

print(f'The number of spaces in the string {sentence} = {spaceCount(sentence)}');
