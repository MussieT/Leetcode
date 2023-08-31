class Solution:
    def findRepeatedDnaSequences(self, s: str) -> list[str]:

        # steps:
            # 1. If the array length is less than 10, return []
            # 2. Start left from 0, right 9, and move both.
            # 3. Set a the values on a hashmap
            # 4. If the new value is on the hashmap, add to the list

        store = dict()
        right = 10
        newList = []

        if len(s) < 9:
            return []

        for left, _ in enumerate(s):
    
            sbstr = s[left:right]

            if sbstr in store:

                if store[sbstr] == 0:
                    newList.append(sbstr)
                    store[sbstr] += 1
                
            else:
                store[sbstr] = 0
            
            right += 1

            if right > len(s):
                break

        return newList

mySolution = Solution()
mySolution.findRepeatedDnaSequences("AAAAAAAAAAA")
