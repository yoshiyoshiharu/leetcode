N = int(input())

count = 0
for i in range(1 , N+1) :
    length = len(str(i))
    if length % 2 == 1 :
        count += 1

print(count)
