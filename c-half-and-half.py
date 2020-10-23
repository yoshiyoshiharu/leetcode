s = input().split(" ")

A = int(s[0])
B = int(s[1])
C = int(s[2])
X = int(s[3])
Y = int(s[4])

#Cの枚数で場合分け
ans =X*A + Y*B
for c in range(0 , max(X,Y)*2+1): #全部Cを頼むのは、2*max(X,Y)のとき
    a = X - (c // 2) #必要なAピザの枚数
    b = Y - (c // 2) #必要なBピザの枚数
    if(a < 0) :
        a = 0
    if (b < 0) :
        b = 0
    price = (A * a) + (B * b) + (C * c)
    ans = min(ans , price)

print(ans)
