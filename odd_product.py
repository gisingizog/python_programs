#Compute the product of all odd numbers between 1 and 20.
product = 1;
for x in range(1,20):
    if( x%2 != 0):
        print("X: " +str(x));
        product *= x;
print("The product of odd numbers less than 20: " + str(product));