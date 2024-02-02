# Write a program which accepts the radius of a circle from the user
# and compute the area and circumference. The area and circumference
# must be in separate functions.

PI = 3.14
area = lambda radius : PI * radius ** 2;
circumference = lambda radius : PI * radius * 2;

radius = float(input('Radius: '));

print(f'\nRadius: {radius}\nArea: {area(radius)}\nCircumference: {circumference(radius)}');