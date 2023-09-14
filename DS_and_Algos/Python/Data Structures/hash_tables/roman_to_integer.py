class Solution:
    def intToRoman(self, num: int) -> str:
        romanStore = {
            1: 'I',
            5: 'V',
            10: 'X',
            50: 'L',
            100: 'C',
            500: 'D',
            1000: 'M'
        }

        if num + 1 in romanStore:
            return romanStore[1] + romanStore[num + 1]
    
        return romanStore[1]
    
mySol = Solution()
print(mySol.intToRoman(4))
