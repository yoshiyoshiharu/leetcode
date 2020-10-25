import math
import sys
N = int(input())


for a in range(1 , 100):
    for b in range(1 , 100):
        if 3**a + 5**b == N :
            print(a , b)
            sys.exit()

print("-1")
