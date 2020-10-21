from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for i in range(len(nums)):
            if target <= nums[i] :
                return i
        else:
            return i + 1
solution = Solution()
print(solution.searchInsert([1,3,5,6] , 0))
