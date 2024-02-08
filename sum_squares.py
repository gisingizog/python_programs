#Square of the sums
#Sum of the squares
def sum_Squares_Diff(number):
    squares_Sum = 0;
    sum_Squares = 0;
    sum = 0;
    for i in range(1, number + 1):
        sum_Squares += i**2;
        sum += i;
    squares_Sum = sum ** 2;
    print(f'Sum of Squares: {sum_Squares}\nSum of numbers: {sum}\nSquare of the sum: {squares_Sum}');
    diff = squares_Sum - sum_Squares;
    return diff

highNumber = int(input('Enter the highest number: '));
print(sum_Squares_Diff(highNumber));
    