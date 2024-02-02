# John is 1,000,000,000 seconds old; how old is John in terms of Years.

seconds = 1000000000;
def secondsToYears(seconds):
    oneyear = 31536000;
    num_Years = seconds / oneyear;
    return num_Years;

print(f'{seconds} seconds = {secondsToYears(seconds)} years')