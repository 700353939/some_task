import time
from random import choice

start = time.time()
numbs = [int(x) for x in input().split()]
target_numb = int(input())

while len(numbs) > 1:
    x = choice(numbs)
    numbs.remove(x)
    y = choice(numbs)
    numbs.remove(y)

    if x + y == target_numb:
        print(f"{x} + {y} = {target_numb}")
    else:
        numbs.append(x)
        numbs.append(y)

end = time.time()
print(f"Time range: {end-start}")