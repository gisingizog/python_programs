# Given a, b,c indices of a quadratic function , find the roots x1, x2 of
# the equation using the following:
import math;


def quadratic():
    values = input('Enter the 3 coefficients: ').split(' ');
    a, b, c = values;
    a = float(a);
    b = float(b);
    c = float(c);
    delta = b**2 - 4*a*c;

    if delta < 0:
        return 'No solution';

    x1 = (-b + math.sqrt(delta))/ 2*a;
    x2 = (-b - math.sqrt(delta))/ 2*a;

    print(f"Coefficients: a: {a}, b: {b}, c:{c}");
    print(f"Roots: root1: {x1}, root2:{x2}");

quadratic();
