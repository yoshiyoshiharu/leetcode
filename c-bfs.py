#最短経路 →　幅優先探索

from collections import deque

R ,C = map(int , input().split())

sy , sx = map(int , input().split())
gy , gx = map(int , input().split())

c = []
c = [list(input()) for i in range(R)]



q = deque([[sy,sx]])

d = []
for _ in range(R) :
    d.append([-1]*C)

moves = [[0,1] , [1,0] , [-1,0] , [0,-1]]
d[sy-1][sx-1] = 0
while q :
    now = q.popleft()

    now_y = now[0]-1
    now_x = now[1]-1


    for move in moves :
        move_y = now_y + move[1]
        move_x = now_x + move[0]

        if c[move_y][move_x] == "." and d[move_y][move_x] == -1 :
            q.append([move_y+1 , move_x+1])
            d[move_y][move_x] = d[now_y][now_x] + 1
            if move_y == gy-1 and move_x == gx-1 :
                print(d[move_y][move_x])
