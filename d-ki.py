N , Q = map(int , input().split())

edge = [[] for _ in range(N+1)]

for _ in range(N-1) :
    a , b = map(int , input().split()) #a-b
    edge[a].append(b) #aにつながる頂点にbを追加
    edge[b].append(a) #bにつながる頂点にaを追加


P = [0]*(N+1)
for _ in range(Q) :
    p,x = map(int , input().split())
    P[p] += x



from collections import deque

q = deque([1])
visited = [False] * (N+1)
visited[0] = True

#幅優先探索
while q :
    print(q)
    now = q.popleft() #前から取り出す
    visited[now] = True
    point = P[now]
    for children in edge[now] : #隣接点に対して
        if not visited[children] :
            P[children] += point
            q.append(children)

for i in range(1,N+1) :
    print(P[i] , end=" ")
