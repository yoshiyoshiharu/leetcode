import sys

H , W = map(int , input().split())

c = [list(input()) for i in range(H)]



def dfs(x,y):
    #xが範囲外 or yが範囲外 or (x,y)が壁
    if not(0 <= x < H) or not(0 <= y < W) or c[x][y] == "#" or c[x][y] == "+":
        return
    #goalならYESを出力して終了
    if c[x][y] == "g":
        for i in range(H) :
            print(str(c[i]))
        print("Yes")
        sys.exit()


    c[x][y] = "+" #操作済みを+にする
    dfs(x+1,y)#下
    dfs(x-1,y)#上
    dfs(x,y+1)#右
    dfs(x,y-1)#左

for i in range(H) :
    for j in range(W) :
        if c[i][j] == "s" :
            sx , sy = i , j

dfs(sx , sy)
print("No")
