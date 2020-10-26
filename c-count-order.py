from itertools import permutations

def main():
    N = int(input())
    P = tuple(map(int , input().split()))
    Q = tuple(map(int , input().split()))
    nums = []
    for i in range(1,N+1):
        nums.append(i)

    per = permutations(nums , N)
    a = 0
    b = 0
    if P == Q :
        return 0
    for i,seq in enumerate(per):
        if seq == P:
            a = i
        elif seq == Q:
            b = i
    else:
        ans = abs(a-b)
        return ans



print(main())
