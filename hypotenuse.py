#Write a function that prints all integer pairs(a,b) greater than 1 and less
# than 100 that can satisfy the hypotenuse rule. Hypotenuse should be
# also integer. Display the number of pairs found. Treat (3,4) and (4,3) as
# one pair

import math;
def hypotenuse():
    count = 0;
    for x in range(1,100):
        for y in range(1,100):
            hyp_Squared = x**2 + y**2;
            hyp = math.floor(math.sqrt(hyp_Squared));
            if hyp_Squared == hyp ** 2:
                if x <= y:
                    print(f"({x},{y})");
                    count += 1;
    print(f"\nTotal pairs: {count}");

hypotenuse();
