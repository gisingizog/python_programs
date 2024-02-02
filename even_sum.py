#Compute the sum of all even numbers less than 100
sum = 0;
i = 0;
while (i<100):
    sum= sum + i;
    print("Value of I: " + str(i));
    i = i+2;
    print('Sum of even numbers less than 100: ' + str(sum));