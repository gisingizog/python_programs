def isCentered(array):
    arr_len = len(array)
    if(arr_len % 2 != 0):

        middle_Index = (arr_len - 1) // 2;
        min_Elt = min(array);

        if array[middle_Index] == min_Elt:
            return True;
        else:
            return False
    else:
        return False;

numbers = input('Enter array values:').split(' ');
numbers = [int(char) for char in numbers]
print (isCentered(numbers));

            