class Solution:
    def reverse(self , x: int) -> int:
        x_strs = str(x)
        if x >= 0 :
            reverse_strs = x_strs[::-1]
        else :
            temp = x_strs[1:]
            temp2 = temp[::-1]
            reverse_strs = '-' + temp2
        if int(reverse_strs) >= 2**31-1 or int(reverse_strs) <= -2**31:
            return 0
        else:
            return int(reverse_strs)

solution = Solution()

print(solution.reverse(-1243))
