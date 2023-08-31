class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        # steps:
            # 1. Initialize left as 0, then move the right.
            # 2. If the character is not found, move the right and update max based on right - left (abc ( right - left + 1 => since it is index 0))
            # 3. If the character is found in charSet, move the left.
            # 4. Move the left until the charSet does not have the character.
            # 5. Move the right, and repeat from 2

        left, maxLength = 0, 0
        charSet = set()

        for right in range(len(s)):
            
            while s[right] in charSet:
                charSet.remove(s[left])
                left += 1
            
            charSet.add(s[right])
            maxLength = max(maxLength, right - left + 1)
            print(f"max len: {maxLength} and substr {charSet}")

myclass = Solution()
myclass.lengthOfLongestSubstring("pwwkew")
