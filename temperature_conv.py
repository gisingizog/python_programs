# Write a program in Python with a function to convert temperature in
# Celsius to Fahrenheit.
# Hints
# How to convert Celsius temperatures to Fahrenheit
# Multiply the Celsius temperature by 9/5.
# Add 32 to adjust for the offset in the Fahrenheit scale.

value = input('Enter the temperature value: ');
unit = input('Unit (C/F): ')

value = float(value);

celsius = lambda fahrenheit : (fahrenheit - 32) * 5/9;
fahrenheit = lambda celsius : (celsius + 32) * 9/5;

if unit.upper() == 'C':
    print(f"Temperature in Celsius: {value}\nTemperature in Fahrenheit: {fahrenheit(value)}");
elif unit.upper() == 'F':
    print(f"Temperature in Celsius: {value}\nTemperature in Fahrenheit: {celsius(value)}");
else:
    print('Invalid Unit');

