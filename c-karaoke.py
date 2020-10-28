'''
1グループN人
M個の曲から選べる
i番目の人が曲jを歌うとAij点取ります

M曲の中から2つ選び(T1,T2)、生徒がT1,T2を歌う。
各生徒の得点はmax(T1,T2)
グループの得点はsum(生徒の得点)

選び方=>MC2 = M(M-1)/2 ~ 5000
'''
from itertools import combinations
N , M  = map(int , input().split())
points = []
for _ in range(N) :
    A_i = list(map(int , input().split()))
    points.append(A_i)

#[[37, 29, 70, 41], [85, 69, 76, 50], [53, 10, 95, 100]]
#points[[point],[point],[point]]
#print(points)

com = combinations(list(range(M)) , 2)
ans = 0
for seq in com:
    total = 0
    for point in points:
        T1 = seq[0]
        T2 = seq[1]
        score = max(point[T1] , point[T2])
        total += score
    else:
        ans = max(ans , total)
print(ans)
