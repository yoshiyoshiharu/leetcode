N = int(input())

nums = 0
for i in range(1 , N+1) :
    count = 0 #約数の数
    for j in range (1 , i+1) :
        if i % j == 0 :
            count += 1


    if (count == 8) and (i % 2 == 1):
        nums += 1
print(nums)
