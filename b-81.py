#9*9を全探索

n = int(input())

def judge(n) :
    for i in range(1 , 10):
        for j in range(1 , 10):
            if n == i*j:
                return True

    else :
        return False

if(judge(n)):
    print("yes")
else:
    print("no")
