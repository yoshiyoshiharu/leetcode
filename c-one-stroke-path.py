'''
vがN
sがM
1スタートでそれ以外の(2,3,4...)を順列全探索

'''
from itertools import permutations
def main():
    N,M=map(int , input().split())
    e = []
    for _ in range(M):
        s = list(map(int , input().split()))
        e.append(s)
        e.append(list(reversed(s)))

    per = permutations(list(range(2,N+1)), N-1)

    ans = 0

    for seq in per:
        seq = tuple([1]) + seq
        flag = True
        for i in range(N-1):
            path = []
            path.append(seq[i])
            path.append(seq[i+1])
            if path not in e:
                flag = False
                break
        else:
            if flag:
                ans += 1

    print(ans)
main()
