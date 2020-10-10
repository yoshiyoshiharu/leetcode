class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 :
            return False
        else:
            x = str(x)
            half_len = len(x) // 2
            if half_len == 0 :
                return True
            print(half_len)
            left = x[:half_len]
            right = x[-half_len:]

            print(left)
            print(right)
            if left == right[::-1] :
                return True
            else :
                return False
solution = Solution()

print(solution.isPalindrome(11))
