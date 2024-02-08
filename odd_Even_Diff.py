def oddEvenDiff(array):
    x = 0; #Odd Sum
    y = 0; #Even Sum
    for i in range(len(array)):
        if(array[i] % 2 ==0):
            y += array[i];
        else:
            x += array[i];
    return x - y;

numbers = input('Enter the array elements:').split(' ');
numbers = [int(char) for char in numbers];
print(f'{oddEvenDiff(numbers)}');