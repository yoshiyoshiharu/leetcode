
'''
str = input()
count = 0
max = 0
array = ['A' , 'T' , 'G' , 'C']
for i in range(len(str)) :
    count = 0
    if str[i] in array :
        for j in range(len(str)-i):
            if str[i+j] in array:
                count += 1
            else :
                if max < count :
                    max = count
                break
        else :
            if max < count :
                max = count

print(max)
'''
#解説
#部分文字列はN + N-1 + ... = N(N+1)/2個だから、全探索

S = input()
N = len(S)
ans = 0
for i in range(N) :
    for j in range(i , N) :
        for c in S[i:j+1] :
            if c not in 'AGCT' :
                break
        else :
            ans = max(ans , j - i + 1)
print(ans)
