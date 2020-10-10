class Solution:
    def romanToInt(self, s: str) -> int:
        Roman_dict = {'I':1 , 'V':5 , 'X':10 , 'L':50 , 'C':100 , 'D':500 , 'M':1000}
        Special_dict = {'IV':4,'IX':9,'XL':40,'XC':90,'CD':400,'CM':900}
        num = 0
        for key , value in Special_dict.items():
            if key in s :
                s = s.replace(key , '')
                num += value

        for string in s :
            if string in Roman_dict.keys() :
                s = s.replace(string , '' , 1)
                num += Roman_dict[string]
        return num

solution = Solution()
print(solution.romanToInt('IV'))
