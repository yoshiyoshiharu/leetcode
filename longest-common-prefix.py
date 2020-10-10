from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0 :
            return ""
        min_str = min(strs , key=len)
        #7->6->5->...->1
        for i in reversed(range(1 , len(min_str)+1)) :
            search_str = min_str[0:i]
            for str in strs :
                if search_str not in str[0:len(search_str)] :
                    break;
            else :
                return search_str
        else :
            return ""
solution = Solution()

print(solution.longestCommonPrefix(["ca" , "a"])
)
