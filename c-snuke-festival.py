
import bisect
def main():
    N = int(input())

    A = list(map(int , input().split()))
    B = list(map(int , input().split()))
    C = list(map(int , input().split()))

    A.sort()
    B.sort()
    C.sort()

    # A_i < B_j < C_kなるi,j,kの数を求める
    # 各B_jに対して、A_i < B_j　を満たす数とB_j < C_k　を満たす数の積
    # これらの総和

    ans = 0
    for b in B :
        A_i = bisect.bisect_left(A,b)
        B_j = bisect.bisect_right(C,b)

        if A_i > 0 and B_j != len(C):
            ans += A_i *  (N - B_j)

    print(ans)
main()
