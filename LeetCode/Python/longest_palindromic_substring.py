# URL: https://leetcode.com/problems/longest-palindromic-substring/description/

"""
Expand around center technique:
Time complexity: O(n²)
Space complexity: O(1)
"""

def lps(s: str) -> str:

    if not s or len(s) == 0:
        # edge case
        return ""
    
    lpoint = 0
    rpoint = 0
    maxlen = 0

    for i in range(len(s)):

        odd_len = palindrome_len(s, i, i)
        even_len = palindrome_len(s, i, i+1)
        maxlen = max(odd_len, even_len)

        # +1 because we are computing the length
        if maxlen > rpoint - lpoint + 1:

            # //2 because we divide towards lower (not towards 0 as int(a/b))
            # -1 to fix offset at the beginning [0]
            lpoint = i - (maxlen-1)//2
            rpoint = i + maxlen//2

    # +1 to add "rpoint" index too
    return s[lpoint:rpoint+1]

def palindrome_len(s: str, lpoint: int, rpoint: int) -> int:

    while lpoint>=0 and rpoint <len(s) and s[lpoint] == s[rpoint]:
        rpoint+=1
        lpoint-=1

    # -1 because we are computing the length
    return rpoint - lpoint -1

if __name__ == "__main__":

    print(lps("babad"))
    print(lps("cbbd"))