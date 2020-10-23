s = input().split(' ')
A = int(s[0])
B = int(s[1])
K = int(s[2])
k=0
for i in reversed(range(1 , 101)) :
    if (A % i == 0 )and(B % i == 0) :
        k += 1
        if k == K :
            print(i)
            break
