'''
For expensive operations, caching the results in a lookup table speeds
future queries.

The lookup table can be built in advance by iterating over all values in
the _domain_ of the function and recording the results.

Or, more lazily, can be build as the individual values are passed in.
'''
import math
import random

# if x = 2 and y = 3
def slowfun_too_slow(x, y):
    # math.pow returns the base to the exponenet eg. pow(27,1/3) = 3
    # 2^3 = 8
    
    v = math.pow(x, y)
    # a factorial is the product of an integer and all the integers below it;
    # e.g. factorial four ( 4! ) is equal to 24. 4x3 + 4x2 + 4x1 = 24
    v = math.factorial(v)

    # // is floor division, ie 9/2=4
    #40320 // 5 = 8064
    v //= (x + y)
    # % takes the remainder
    v %= 982451653

    return v

cache = {}
def slowfun(x, y):
    """
    Rewrite slowfun_too_slow() in here so that the program produces the same
    output, but completes quickly instead of taking ages to run.
    """
    # Your code here
    # need to use caching
    key = f'{x}{y}'
    if key not in cache:
        v = math.pow(x, y)
        v = math.factorial(v)
        v //= (x + y)
        v %= 982451653
        cache[key] = v

        return cache[key]

    else:
        return cache[key]
    



# Do not modify below this line!

for i in range(50000):
    x = random.randrange(2, 14)
    y = random.randrange(3, 6)
    print(f'{i}: {x},{y}: {slowfun(x, y)}')

# import math
# math.pow(2,3)
# math.factorial(8)

# 40320 //5

# key = f'{2}{3}'
# print(key)