# Write a program in Python to find the Area and Perimeter of a Rectangle.
# You should get the width and length from the user through the
# keyboard.

parameters = input('Length & Width: ').split(' ');
length , width = parameters;

length = float(length);
width = float(width);

area = lambda a,b : a*b;
perimeter = lambda a,b : (a + b) *2;

print(f" Length: {length} Width: {width}\n Area: {area(length,width)} Perimeter: {perimeter(length,width)}");

