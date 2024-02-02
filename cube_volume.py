# Write a function to compute the volume of the cube on user input.

side = float(input('Side of cube= '));
volume = lambda side: side ** 3;
print(f'\nSide: {side}\nVolume: {volume(side)}');