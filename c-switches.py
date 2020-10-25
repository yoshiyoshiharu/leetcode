N , M  = map(int , input().split())

k = []
s = []
for i in range(M) : # 電球ごとのループ
    ks = list(map(int , input().split()))

    k.append(ks[0]) #電球がつながるスイッチの数

    s.append(ks[1:]) #二重リストでつながっているスイッチの番号

p = list(map(int , input().split())) # その電球につながったスイッチのonの数が奇数or偶数

ans = 0
for i in range(2 ** N) :#スイッチごとのループ (0,1,0)など
    switch = [0] * N

    for j in range(N) :
        if ((i >> j) & 1) :
            switch[N - 1 - j] = 1
    judge = True
    for light in range(M) : #各電球に対して
        count = 0 #その電球につながったonスイッチ数
        for l in range(k[light]) : #その電球につながっているスイッチに対して
            if switch[l] == 1 :
                count += 1

        if count % 2 != p[light] : # 電球につながったonの数％２がpに等しくないなら
            judge = False #その時点で終了→次の電球へ
            break
    if judge :
        ans += 1
print(ans)
