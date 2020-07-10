
# hint - In Python, a dict key can be any immutable type... including a tuple.

# SAME AS LOOKUP_TABLE

lookup = {}

def expensive_seq(x, y, z):
    
    if x <= 0:
        return y + z
    elif x >  0:
        key = f'{x}{y}{z}'
        if key not in lookup:
            lookup[key] = expensive_seq(x-1,y+1,z) + expensive_seq(x-2,y+2,z*2) + expensive_seq(x-3,y+3,z*3)
            return lookup[key]
        else:
            return lookup[key]




if __name__ == "__main__":
    for i in range(10):
        x = expensive_seq(i*2, i*3, i*4)
        print(f"{i*2} {i*3} {i*4} = {x}")

    print(expensive_seq(150, 400, 800))
