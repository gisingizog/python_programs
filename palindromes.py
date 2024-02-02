# A function is required that checks strings to see if they are
# palindromes. A palindrome string that reads the same, backwards, or
# forwards. 

value = input('Enter a string: ');

#Without built in functions
reversed_Text = value[::-1]
print(f'Is {value} a palindrome? {value == reversed_Text}');

#With some built in functions like len
def isPalindrome(value):
    i = len(value) - 1;
    reversedValue = '';
    while i >= 0:
        reversedValue += (value[i]);
        i -= 1;
    if value == reversedValue :
        return True;

print(f'Is {value} a plaindrome? {isPalindrome(value)}');

#With built in func
reversed_String = ''.join(reversed(value));
print(f'Is {value} a palindrome? {value == reversed_String}')
