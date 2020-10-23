'''
約数は、(A, B) = (B ,A)が成り立つから、√N回のループでよい
'''

N = int(input())

i = 1
ans = 10
while(i*i <= N) :
    if N % i == 0:
        digits = len(str(int(N/i)))
        ans = min(ans , digits)
    i += 1

print(ans)
