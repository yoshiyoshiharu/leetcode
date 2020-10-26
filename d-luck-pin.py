
from itertools import combinations
def main():
    N = int(input())
    S = tuple(input())#編集不可の定数
    ans = 0
    for i in range(1000):
        nums = list(S)
        pin = str(i).zfill(3)
        flag = 0
        if pin[0] in nums:
            j = nums.index(pin[0])+1
            nums = nums[j:]
            flag += 1

        if pin[1] in nums:
            j = nums.index(pin[1])+1
            nums = nums[j:]
            flag += 1
        if pin[2] in nums:
            j = nums.index(pin[2])+1
            nums = nums[j:]
            flag += 1
        if flag == 3:
            ans += 1
    print(ans)
main()
