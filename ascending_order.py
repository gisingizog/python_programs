# Write a function to read three integers and to print them in ascending
# order
values = input('Enter the three numbers: ').split(' ');

def swap(a,b):
    temp = a;
    a = b;
    b = temp;

def ascending_Order(values):
    i = 0;
    while(i < len(values)):
        if(values[i] > values[i]) :
            temp=values[i];
            values[i] = values [i+1];
            values[i+1]= temp;
            i += 1;
        else:
            i += 1;
    return values;

sorted_List = ascending_Order(values);
print(sorted_List);


