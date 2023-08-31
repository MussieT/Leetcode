class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        # steps:
            # 1. start with the first letter
            # 2. if the upcoming ones are the same, then .. update the right
            # 3. if the upcoming letter is different..replace it with the first and subtract k
            # 4. if k is not 0 and right goes to end .. go the left direction of the starting letter.

        left = 0
        charSet = dict()
        maxLength = 0

        charSet.add("a")
        charSet.add("a")

        print(f"the upper charset: {charSet}")

        for right in range(len(s)):
            first_elemment = s[right]
            
            j = 0
            while k > 0:
            #    print(f"here i am {k}")

               if first_elemment != s[j]:
                  k -= 1
               
               j += 1

               print("k is : ", charSet)
            
            charSet.clear()
            
            if k == 0:
                k += 2

            maxLength = max(maxLength, len(charSet))
        
        print("max length is: ", maxLength)

        return k
    
myClass = Solution()
myClass.characterReplacement("abaab", 2)