from itertools import permutations
import math
N = int(input())

p  =[]
town = []
for _ in range(N) :
    s = list(map(int , input().split()))
    p.append(s)

for i in range(0 , N) :
    town.append(i)



per = permutations(town , N)
ave = 0
for pattern in per :
    for i in range(N-1):
        before = pattern[i]
        after = pattern[i+1]
        ave += ((p[after][0]- p[before][0])**2 + (p[after][1]- p[before][1])**2)**(1/2)


ave /= math.factorial(N)

print(ave)
