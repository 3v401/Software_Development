# URL: https://leetcode.com/problems/find-all-anagrams-in-a-string/description/

'''
There will be 3 situations in the code:

    1. The window is getting bigger and we add characters
    2. The window is full and we must move to the right (delete leftmost element)
    3. The number of elements in the window is enough and the anagram is found
'''

from collections import Counter

class Solution:
    def faaias(self, s: str, p: str) -> list[int]:

        if len(p)>len(s):
            # edge case
            return []

        needed = Counter(p)
        matches = 0
        m= len(p)
        lpoint = 0
        res: list[int] = []
        # answer of the program

        for rpoint, char in enumerate(s):

            # expand and add to the window
            if char in needed:
                needed[char] -= 1
                if needed[char] == 0:
                    # if we reach 0 elements in needed, match for a letter
                    matches +=1
            # if length of window surpassed
            if rpoint - lpoint + 1 > m:
                outer_char = s[lpoint]
                if outer_char in needed:
                    # if leftmost char is required
                    if needed[outer_char] == 0:
                        matches -=1

                    needed[outer_char] +=1
                lpoint+=1

            # if length of window is enough, and matches == len(needed)
            if rpoint - lpoint + 1 == m and matches == len(needed):
                # When there are enough elements and frequencies in the window -> anagram found
                res.append(lpoint)
                # add index beginning
        return res
    
if __name__ == '__main__':

    sol = Solution()
    print(sol.faaias("cbaebabacd", "abc"))
    print(sol.faaias("abab", "ab"))