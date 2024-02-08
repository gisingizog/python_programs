# Write a function named minDistance that returns the smallest positive
# distance between two factors of a number. For example, consider the
# number 13013. Its factors are 1, 7, 11, 13, 77, 91, 143, 169, 1001, 1183, 1859
# and 13013.

def minDistance(number):
    factors=[];
    min_dist = float('inf');
    j = 0;
    #Loop to find the factors
    for i in range(1,number + 1):
        if number % i == 0:
            factors.append(i);
   
    #Find the difference
    
    for j in range(len(factors) - 1):
        diff = factors[j+1] - factors[j]
        if diff < min_dist:
            min_dist = diff
            j += 1
    return min_dist;

num = int(input('Enter any number: '));
print(f'The smallest disstance between two factors is {minDistance(num)}');

