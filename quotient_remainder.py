# Write a program with a function to compute quotient and remainder of
# two numbers accepted from keyboard.

quotient = lambda a,b : a/b;
remainder = lambda a,b: a%b;

operands = input("Operands: ").split();
a,b = operands;

a = float(a);
b= float(b);

print(f"Quotient: {quotient(a,b)}");
print(f"Remainder: {remainder(a,b)}");