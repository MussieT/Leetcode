class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        strs2 = []
        wordHash = {}
        
        for val in strs:

            # sort every element in the array
            sortedString = ''.join(sorted(val))
            
            if sortedString in wordHash:
                wordHash[sortedString].append(val)
            else:
                wordHash[sortedString] = [val]

        print("word hash: ", wordHash)

        # since we can't return the hashMap
        for _, value in wordHash.items():
            strs2.append(value)
        
        print("str : ", strs2)

        return strs2

myClass = Solution()
print(myClass.groupAnagrams(["a"]))