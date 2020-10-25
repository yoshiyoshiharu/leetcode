
def main():
    N = int(input())
    s = []
    for _ in range(N):
        A = int(input())
        evi = [] #その人の証言
        for _ in range(A) :
            xy = list(map(int , input().split()))
            evi.append(xy)
        else:
            s.append(evi)

    # print("入力データ:",s)
    # ここまでが入力
    ans = 0
    for i in range(2 ** N) :
        array = [0]*N
        for j in range(N) :
            if((i >> j) & 1) :
                array[N-1-j] = 1
        #この時点で、array = [0,1,0]みたいになってる
        flag = True
        for k in range(N):
            if not flag:
                break
            flag = True
            if array[k] == 1 :#k番目の人がhonestなら
                for evi in s[k]: #k番目の人の証言でループ
                    x = evi[0]
                    y = evi[1]
                    if y != array[x-1]: #証言　!= 実際
                        flag = False #矛盾

        else:#すべての人の証言が合っていたら
            if flag:
                ans = max(ans , sum(array))
    print(ans)
main()
