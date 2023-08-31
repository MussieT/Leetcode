class Solution:
    def findSubstring(self, s: str, words: list[str]) -> list[int]:
        # steps
            # 1. start left 0
            # 2. right - words[i] length
            # 3. move the right by words[i] length
            # 4. if the new substring is among words .. add to hashmap ..
            # 5. if the hashmap length is equal to words length .. store left
            # 6. move the left by words[i] length
            # 7. remove the left element from hashmap
            # 7. If not found till the end of the right .. return ..

            left, right, wordLength = 0, 0, len(words[0])
            store = dict()
            indexStore = []

            right += wordLength

            # move the left with range..
            for left in range(0, len(s), wordLength):
                  
                #   print(f"len of store {left} and len of s {len(s)} and wordLength: {s[left:right]}")
                  
                #   while right <= len(s):
                sbstr = s[left:right]

                print(f"sbstr: {sbstr}")

                    # if sbstr in words:
                    #     print(f"sbstr {sbstr}")
                    #     store[sbstr] = sbstr

                right += wordLength


            left += right

            print(f"right {store}")

            return []

myClass = Solution()
myClass.findSubstring("aabda", ["da", "bd"])
